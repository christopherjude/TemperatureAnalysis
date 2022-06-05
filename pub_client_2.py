import paho.mqtt.client as mqtt
# This is the Subscriber
#hostname
broker="localhost"
#port
port=1883
#time to live
timelive=120
index = 0
avg_l = []
l = []
avg_i = 0
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("/data")
def on_message(client, userdata, msg):
    global index, avg_l, l, avg_i
    message = msg.payload.decode()
    print(message)
    temperature = message[-2:]
    index += 1
    if index < 5:
        l.append(int(temperature))
    else:
        average = sum(l)/len(l)
        avg_l.append(average)
        avg_i += 1
        print(f"Average {avg_i} : {average}")
        l = []
        index = 0
    
client = mqtt.Client()
client.connect(broker,port,timelive)
client.on_connect = on_connect
client.on_message = on_message
try:
    client.loop_forever()
except KeyboardInterrupt as ki:
    print(f'Stopping client on KeyboardInterrupt.')
    client.disconnect()
    client.loop_stop()