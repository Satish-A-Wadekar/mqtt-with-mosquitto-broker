import logging
import subprocess

logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG) 
logger = logging.getLogger()

try:
    # to run the shellscript via python code
    subprocess.call('/usr/local/sbin/mosquitto -c configuration/mosquitto.conf', shell=True)
    logger.info('mosquitto server is up & running')
except Exception as e:
    print('main > error >', e)
    logger.error(e)
