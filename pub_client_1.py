#simulator device 1 for mqtt message publishing
import paho.mqtt.client as paho
import time
import random
#hostname
broker="localhost"
#port
port=1883
def on_publish(client,userdata,result):
    print("Device 1 : Temperature published.")
    pass
client= paho.Client("admin")
client.on_publish = on_publish
client.connect(broker,port)
i = 0
while True:
    try:
        random_temperature = random.randint(28,38)
        #telemetry to send 
        message="Device 1 : Data " + str(i) + f" => {random_temperature}"
        time.sleep(0.5)
            
        #publish message
        ret= client.publish("/data",message)
    except KeyboardInterrupt as ki:
        print(f'Stopping script with KeyboardInterrupt.')
        break
print("Stopped...")