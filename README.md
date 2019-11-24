# Melget 

This library allows to connect to the Mitsubishi Cloud library in order to read and write the setup of an 
Mitsubishi AC device. 

## Getting Started

The requirements to allow handling this device are: a Mitsubishi split, that supports the MAC-567IF-E interface.
See http://library.mitsubishielectric.co.uk/pdf/search/MAC-567IF, and Mistubishi Melcloud account, https://www.melcloud.com/ 

### Prerequisites

Our AC device, will be registered in the Melcloud plattform, in order to be used by our library.

For example:
The device:
![MyLivingRoomAC](https://fcopuerto.github.io/docs/melget/MyLivingRoom.png) which is setup in the builindg myBulding, can be controlled with the API:
![MyLivingRoomAC](https://fcopuerto.github.io/docs/melget/MyLivingRoomAC_Details.png)


### Installing

This serverless library, should be deployed as a Lambda, runing Python 3.7 in AWS. 
Tha handler of this lambda will be lambda_function.lambda_handler and this lambda needs the login of melclooud as
a environment vars, this code is done in order to decrypt thos parameters that should be encrypted in the lambda as with an AWS KMS key.

Example of environment keys:
```
"MELCLOUD_USER": "****************************************"
"MELCLOUD_PASS": "****************************************"
```

This library was mad to bein used from Amazon Alexa https://developer.amazon.com

## Running the tests

Not available yet

### Break down into end to end tests

Not available yet

```
Give an example: Not available yet
```

### And coding style tests

Not available yet

```
Give an example: Not available yet
```

## Deployment

See deploy.yml file.

## Built With

* [Python3](https://docs.python.org/release/3.7.3/) - The main code used
* [AWS Lambda](https://aws.amazon.com/es/lambda/) - The serverless infrastucture


## Contributing

Please read [CONTRIBUTING.md](https://fcopuerto.github.com/) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Fran Puerto ** - *Initial work* - (https://github.com/fcopuerto)

See also the list of [contributors](https://github.com/fcopuerto/melget/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* This driver is not official, so it's done with reverse engineering, because Mitsubishi didn't publish its Melcloud API.
* Soon updates and Alexa integration

