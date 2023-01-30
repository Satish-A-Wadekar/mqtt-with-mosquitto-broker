from dotenv import load_dotenv
import os
import logging
import paho.mqtt.client as mqtt

load_dotenv()
logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG) 
logger = logging.getLogger(__name__)

try:
    def on_log(client, user_data, level, buf):
        logger.info(" log: ", buf.decode("utf-8"))
        
    print("creating new client instance")
    client = mqtt.Client(
        client_id="Publisher_Hub", 
        clean_session=True, 
        userdata=None, 
        #protocol="MQTTv311", 
        transport="tcp",
        reconnect_on_failure=True
    )
    
    print("connecting to broker")
    client.connect(
        host=os.getenv('HOST'), 
        port=int(os.getenv('PORT')), 
        keepalive=60, 
        bind_address=""
    )
    
    print("loop_start")
    client.loop_start()  # start the loop
    
    print("publishing message to topic")
    client.publish(
        topic=os.getenv('TOPIC'), 
        payload='Published from python', 
        qos=0, 
        retain=False
    )
    client.on_log = on_log
    
    client.loop_stop()
    print("loop_stop")
    
except Exception as e:
    logger.error('main > errorType >', type(e))
    logger.error('main > errorMessage >', e.args)
    logger.error('main > error >', e)
    