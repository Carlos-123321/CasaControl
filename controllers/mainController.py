import os
from flask import Blueprint, render_template, request, jsonify
from mqtt_client import mqtt_client, mqtt_command_topic, status_message

main_bp = Blueprint('main_controller', __name__)

@main_bp.route('/')
def home_func():
    return render_template('home.html')

@main_bp.route('/lamp-confirmation', methods=['GET', 'POST'])
def control_led():
    if request.method == 'POST':
        command = request.form['command']
        if command.lower() in ["on", "onal"]:
            mqtt_client.publish(mqtt_command_topic, command)
            return f"Sent command: {command}"
        else:
            return "Invalid command. Please type 'on' or 'off'."
    return f'''
        <form method="POST">
            Enter command (on/off): <input type="text" name="command">
            <button type="submit">Send</button>
        </form>
        <p>Status: {status_message}</p>  <!-- Access status_message here -->
    '''

@main_bp.route('/historical')
def historical_data_func():
    print("historical route")
    return render_template('historical_data.html')

@main_bp.route('/about', methods=['GET', 'POST'])
def about_func():
    global status_message
    if request.method == 'POST':
        command = request.form['command'].strip().lower()

        mqtt_client.publish(mqtt_command_topic, command)
        status_message = f"Command '{command}' sent to Raspberry Pi."

        return render_template('about.html', status_message=status_message)

    return render_template('about.html', status_message=status_message)


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

@main_bp.route('/profile')
def profile_func():
    return render_template('profile.html')