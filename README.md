
# MQTT with Mosquitto broker (Python platform)

- Author: [Satish Wadekar](https://www.linkedin.com/in/satish-4b565056/)
- License: [MIT](https://github.com/Satish-A-Wadekar/mqtt-with-mosquitto-broker/blob/main/LICENSE "MIT")
- Repo URL: [https://github.com/Satish-A-Wadekar/mqtt-with-mosquitto-broker](https://github.com/Satish-A-Wadekar/mqtt-with-mosquitto-broker)
- Contacts: satish.a.wadekar@gmail.com
- Requirements: Python, Mosquitto server

## Features
This is a very quick & simple boilerplate where you can develop python app with MQTT protocols for Pub/Sub message exchange module with the help of Mosquitto broker (custome configuration)

## Installation

#### You need to install Mosquitto broker server on your machine to run this project locally, to install Mosquitto you can check this link https://mosquitto.org/download/. 
Mosquitto can be installed from the homebrew project

```
  brew install mosquitto
```

Create virtual environment for your Python project

```
  python3 -m venv your_env_name
```
 
Activate the virtual environment

```
  source your_env_name/bin/activate
```
 
Install all dependencies 

```
  pip install -r requirements.txt
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

if you face any error while server starting, just kill all previously running mosquitto servers at your local. to do this just run following command
```bash
killall mosquitto
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

## Support

For support, email satish.a.wadekar@gmail.com.

