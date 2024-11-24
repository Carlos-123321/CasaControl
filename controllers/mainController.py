import os

from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from Models.models import Project, db, Task

main_bp = Blueprint('main_controller', __name__)

@main_bp.route('/')
def home_func():
    return render_template('home.html')



@main_bp.route('/historical')
def historical_data_func():
    print("historical route")
    return render_template('historical_data.html')

@main_bp.route('/about')
def about_func():
    return render_template('about.html')

@main_bp.route('/contact')
def contact_func():
    return render_template('contact.html')

@main_bp.route('/historical-data')
def historical_data():
    print("route first")
    data = read_historical_data()
    return jsonify(data)

def read_historical_data():
    historical_data = []
    file_path = 'Data/historical_data.txt'

    print("Hello world")

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                timestamp, value = line.strip().split(',')
                print("exec" + timestamp, value)
                historical_data.append({'timestamp': timestamp, 'value': float(value)})
    return historical_data

@main_bp.route('/liveData')
def live_data_func():
    return render_template('live_data.html')

@main_bp.route('/live-data')
def get_sensor_data():
    print("Sending sensor data:", sensor_data)
    return jsonify(sensor_data)

sensor_data = {"temperature": [], "humidity": []}

def on_message(client, userdata, msg):
    print("Received MQTT message:", msg.payload)
    data = msg.payload.decode().split(',')
    temperature, humidity = float(data[0]), float(data[1])
    sensor_data["temperature"].append(temperature)
    sensor_data["humidity"].append(humidity)

def saveDataToList(temperature, humidity):
    sensor_data["temperature"].append(temperature)
    sensor_data["humidity"].append(humidity)