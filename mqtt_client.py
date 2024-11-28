import paho.mqtt.client as mqtt

BROKER = "rpi2024"
PORT = 1883
COMMAND_TOPIC = "home/commands"
STATUS_TOPIC = "home/status"

status_message = ""

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(STATUS_TOPIC)


def on_message(client, userdata, msg):
    global status_message
    status_message = msg.payload.decode()
    print(f"Status update: {status_message}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_start()


mqtt_client = client
mqtt_command_topic = COMMAND_TOPIC
mqtt_status_topic = STATUS_TOPIC
