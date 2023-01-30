
# MQTT with Mosquitto broker

This is a very quick & simple boilerplate where you can develop python app with MQTT protocols for Pub/Sub message exchange module with the help of Mosquitto broker (custome configuration)




## Tech Stack

**Server:** Python, Mosquitto


## Installation

#### You need to install Mosquitto broker server on your machine to run this project locally, to install Mosquitto you can check this link https://mosquitto.org/download/. 
Mosquitto can be installed from the homebrew project

```
  brew install mosquitto
```

Create virtual environment for your Python project

```http
  python3 -m venv your_env_name
```
 
Activate the virtual environment

```http
  source your_env_name/bin/activate
```
 
Install all dependencies 

```http
  python3 install -r requirements.txt
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file. 
I have already added env-template file in repo which you can use for your .env file setup

`HOST`

`PORT`

`USERNAME`

`PASSWORD`

`TOPIC`


## Run Locally 
#### Open 3 different terminal windows & run following commands on each separately    

first run main.py to start the mosquitto server

```bash
  python3 main.py
```

on second terminal window run subscriber code 

```bash
  python3 src/mqtt_sub.py
```

then on third terminal window run publisher code

```bash
  python3 src/mqtt_pub.py
```



## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Author

- [Satish Wadekar](https://github.com/Satish-A-Wadekar)


## Support

For support, email satish.a.wadekar@gmail.com.

