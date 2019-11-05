import json
import requests
import boto3
from datetime import datetime
from datetime import time
from decimal import Decimal
import time as time_
import os
import base64 

def lambda_handler(event, context):

    MELCLOUD_USER = KMSDecrypt(os.environ["MELCLOUD_USER"])
    MELCLOUD_PASS = KMSDecrypt(os.environ["MELCLOUD_PASS"])
    
    StructureName = event['StructureName']
    DeviceName = event['DeviceName']   
    Action = event.get('Action','SAVE')
    Token = doLogin (MELCLOUD_USER, MELCLOUD_PASS)    

    if Action == 'GET':
        Result = getDeviceByID(Token)
    if Action == 'SET':
        Device = getDeviceByID(Token)
        ConsignTemp = event.get('Temperature',None)
        if ConsignTemp is not None:
            Device['SetTemperature'] = ConsignTemp
            Result = SetAta(Token, Device)
    if Action == 'SET_FAN':
        Device = getDeviceByID(Token)
        ConsignFanSpeed = event.get('FanSpeed',None)
        if ConsignFanSpeed is not None:
            Device['SetFanSpeed'] = ConsignFanSpeed
            Result = SetAta(Token, Device)           
    if Action == 'SET_ON':
        Device = getDeviceByID(Token)
        Device['Power'] = True
        Device['EffectiveFlags']= 1
        Result = SetAta(Token, Device)
    if Action == 'SET_ON_AT':
        Device = getDeviceByID(Token)
        Device['Power'] = True
        Device['EffectiveFlags']= 1
        Device['SetTemperature'] = ConsignTemp
        Result = SetAta(Token, Device)
    if Action == 'SET_ON_INC':
        Device = getDeviceByID(Token)
        Device['Power'] = True
        Device['EffectiveFlags']= 1
        Device['SetTemperature'] = Device['SetTemperature'] + ConsignTemp
        Result = SetAta(Token, Device)    
    if Action == 'SET_OFF':
        Device = getDeviceByID(Token)
        Device['EffectiveFlags']= 1
        Device['Power'] = False
        #Device['EffectiveFlags']= 0
        Result = SetAta(Token, Device)    
    if Action == 'SAVE':
        TableDB = 'MelcsDevice'
        Device = getDeviceByID(Token)
        putDB(Device,TableDB)
    return Result

def doLogin(User,Password):
    url = 'https://app.melcloud.com/Mitsubishi.Wifi.Client/Login/ClientLogin'
    body = {
        "AppVersion": "1.18.5.1",
        "CaptchaResponse": None,
        "Email": User,
        "Language": 6,
        "Password": Password,
        "Persist": False
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(body), headers=headers)
    response = response.json()
    LoginData = response.get('LoginData')
    Token = LoginData.get('ContextKey')
    return Token

def getDeviceByID(Token):
    response = requests.get(
    'https://app.melcloud.com/Mitsubishi.Wifi.Client/Device/Get?id=134314&buildingID=77048',
    params={'q': 'requests+language:python'},
    headers={'Host': 'app.melcloud.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-MitsContextKey': Token,
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://app.melcloud.com/',
        'Cookie': 'policyaccepted=true',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'},
    )
    json_response = response.json()
    return json_response    

def getListDevices(Token):
    response = requests.get(
    'https://app.melcloud.com/Mitsubishi.Wifi.Client/User/ListDevices',
    params={'q': 'requests+language:python'},
    headers={'Host': 'app.melcloud.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-MitsContextKey': Token,
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://app.melcloud.com/',
        'Cookie': 'policyaccepted=true',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'},
    )
    json_response = response.json()
    return json_response
    
def getDevices(Token, StructureName):
    Structures = getListDevices(Token)
    for Structure in Structures:
        if Structure['Name'] == StructureName:
            return Structure['Structure']['Devices']

def getDevice (Token, StructureName, DeviceName):
    Devices = getDevices(Token, StructureName)
    for Device in Devices:
        return Device
        if Device['DeviceName'] == DeviceName:
            return Device

def SetAta (Token, Values):
    url = 'https://app.melcloud.com/Mitsubishi.Wifi.Client/Device/SetAta'
    body = Values
    headers = { 'Host': 'app.melcloud.com',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:69.0) Gecko/20100101 Firefox/69.0',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/json; charset=utf-8',
                'X-MitsContextKey': Token,
                'X-Requested-With': 'XMLHttpRequest',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Referer': 'https://app.melcloud.com/',
                'Cookie': 'policyaccepted=true'}
    dt = datetime.utcfromtimestamp((millis()+60000)/1000)  
    body['HasPendingCommand'] = True          
    dtstring = dt.isoformat()+'Z'
    body['NextCommunication'] = dtstring.replace('000Z','')
    print(json.dumps(body))
    response = requests.post(url, data=json.dumps(body), headers=headers)
    #response = response.json()
    #type(response)
    return response.status_code    


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def millis():
    return int(round(time_.time() * 1000))

def putDB(item,tableDB):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableDB)
    ymd = datetime.today().strftime('%Y%m%d')
    timestamp = datetime.now().microsecond
    item['ymd']= ymd
    item['timestamp']= millis()
    response = table.put_item(Item=json.loads(json.dumps(item), parse_float=Decimal))
    print('PutItem succeeded:')
    print(json.dumps(response, indent=4, cls=DecimalEncoder))

def KMSDecrypt(encryptedVar):
    cipherTextBlob = base64.b64decode(encryptedVar)
    decrytedVar = boto3.client('kms').decrypt(CiphertextBlob=cipherTextBlob)['Plaintext']
    return str(decrytedVar, 'utf-8')