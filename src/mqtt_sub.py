from dotenv import load_dotenv
import os
import logging
import time
import paho.mqtt.client as mqtt

logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG) 
logger = logging.getLogger(__name__)
load_dotenv()

try:
    def on_log(client, user_data, level, buf):
        logger.info(" log: ", buf.decode("utf-8"))
        
    def on_message(client, user_data, message):
        print("message received ", str(message.payload.decode("utf-8")))
        print("message topic=", message.topic)
        print("message qos=", message.qos)
        print("message retain flag=", message.retain)
        
    print("creating new client instance")
    client = mqtt.Client(
        client_id="Subscriber_Device", 
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
    
    print("subscribe the topic")
    client.subscribe(os.getenv('TOPIC'))
    client.on_message = on_message  # attach function to callback
    client.on_log = on_log
    
    time.sleep(30)
    client.loop_stop()
    print("loop_stop")
    
except Exception as e:
    print('main > errorType >', type(e))
    print('main > errorMessage >', e.args)
    print('main > error >', e)
    