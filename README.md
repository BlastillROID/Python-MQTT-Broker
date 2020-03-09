# Python MQTT Broker

a Python MQTT client that simulates heat input or distance then sends publishes a message to an MQTT server

## Getting Started

```
[1]: Manual Data Entry
[2]: Temperature Simulation
        Sends Message if T > 40 °C
[3]: Distance Simulation
        Sends Message if you go further than 300 cm
```
Simply choose which Scenario you would like to test

### Prerequisites

* Eclipse [Mosquitto](https://mosquitto.org/download/)
* [Python](https://www.python.org/downloads/)


### Installing

First we need to run our MQTT Mosquitto server from the CMD

```
C:\Program Files\mosquitto\mosquitto.exe -v
```

Then run our client python script

```
& python "b:/FivePoints/MQTT Python/main.py" 
```

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/BlastillROID/Python-MQTT-Broker/tags). 

## Authors

* **Mounir Missaoui** - *Initial work* - [BlastillROID](https://github.com/BlastillROID)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

