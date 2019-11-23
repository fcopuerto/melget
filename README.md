# Melget 

This library allows to connect to the Mitsubishi Cloud library in order to read and write the setup of an 
Mitsubishi AC device. 

## Getting Started

The requirements to allow handling this device are: a Mitsubishi split, that supports the MAC-567IF-E interface.
See http://library.mitsubishielectric.co.uk/pdf/search/MAC-567IF, and Mistubishi Melcloud account, https://www.melcloud.com/ 

### Prerequisites

Our AC device, will be registered in the Melcloud plattform, in order to be used by our library.
```
For example the device MyLivingRoomAC which is setup in the builindg myBulding can be controlled by this API
```

### Installing

This API should be deployed as a Lambda, runing Python 3.7 in AWS. 
Tha handler of this lambda will be lambda_function.lambda_handler and this lambda needs the login of melclooud as
a environment vars, this code is done in order to decrypt thos parameters that should be encrypted in the lambda as with an AWS KMS key.

This library was mad to bein calle from Amazon Alexa https://developer.amazon.com

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

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Fran Puerto ** - *Initial work* - [PurpleBooth](https://github.com/fcopuerto)

See also the list of [contributors](https://github.com/fcopuerto/melget/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This driver is not official, so it's done with reverse engineering, because Mitsubishi didn't publish its Melcloud API.
* Soon updates and Alexa integration

