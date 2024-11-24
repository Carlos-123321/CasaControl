# import mqtt
import paho.mqtt.client as mqtt
from flask import Flask
from config import Config
from controllers.mainController import main_bp, saveDataToList
# from controllers.TasksController import task_bp
from Models.models import db
app = Flask(__name__)
app.config.from_object(Config)
# Initialize the database
# Register Blueprints
app.register_blueprint(main_bp)

# Define the MQTT settings
BROKER = "rpi2024"
PORT = 1883
TOPIC = "home/Sensor"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC)



def on_message(client, userdata, msg):
    data = msg.payload.decode().split(',')
    print(msg.payload.decode())
    temperature, humidity = float(data[0]), float(data[1])
    print("print", temperature, humidity)
    saveDataToList(temperature, humidity)


# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message
# client.connect(BROKER, PORT, 60)
# client.loop_start()


if __name__ == '__main__':
 app.run(debug=True)