import paho.mqtt.client as mqtt
import json

BROKER = "rpi2024"
PORT = 1883
COMMAND_TOPIC = "home/commands"
STATUS_TOPIC = "home/status"
CLIMATE_TOPIC = "home/climate"

status_message = ""
temperature = None
humidity = None

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(STATUS_TOPIC)
    client.subscribe(CLIMATE_TOPIC + "/temperature")
    client.subscribe(CLIMATE_TOPIC + "/humidity")

def on_message(client, userdata, msg):
    global temperature, humidity, status_message
    topic = msg.topic

    if topic == STATUS_TOPIC:
        status_message = msg.payload.decode()
        print(f"Status update: {status_message}")

    elif topic == CLIMATE_TOPIC + "/temperature":
        try:
            temperature_data = json.loads(msg.payload.decode())
            temperature = temperature_data.get('temperature')
            print(f"Received temperature: {temperature}°C")

            if 'flask_app' in globals():
                flask_app = globals()['flask_app']
                with flask_app.app_context():
                    flask_app.config['TEMPERATURE'] = temperature

        except json.JSONDecodeError:
            print("Failed to decode temperature data")

    elif topic == CLIMATE_TOPIC + "/humidity":
        try:
            humidity_data = json.loads(msg.payload.decode())
            humidity = humidity_data.get('humidity')
            print(f"Received humidity: {humidity}%")

            if 'flask_app' in globals():
                flask_app = globals()['flask_app']
                with flask_app.app_context():
                    flask_app.config['HUMIDITY'] = humidity

        except json.JSONDecodeError:
            print("Failed to decode humidity data")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_start()

mqtt_client = client
mqtt_command_topic = COMMAND_TOPIC
mqtt_status_topic = STATUS_TOPIC

def set_flask_app(app):
    global flask_app
    flask_app = app