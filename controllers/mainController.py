from flask import session, url_for, redirect, render_template, request, jsonify, current_app
from flask import Blueprint
import os
from mqtt_client import mqtt_client, mqtt_command_topic, status_message, temperature, humidity

main_bp = Blueprint('main_controller', __name__)

@main_bp.route('/')
def home_func():
    return render_template('home.html')

@main_bp.route('/contact')
def contact_func():
    return render_template('contact.html')

@main_bp.route('/profile')
def profile_func():
    return render_template('profile.html')

@main_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'carlos' and password == 'admin123':
            session['user_verified'] = True
            return redirect(url_for('main_controller.home_func'))

        else:
            return "Invalid credentials, please try again."


@main_bp.route('/lamp-commands', methods=['GET', 'POST'])
def lamp_commands_func():

    if not session.get('user_verified'):
        return redirect(url_for('main_controller.profile_func'))

    global status_message
    valid_lamp_commands = ["onll", "offll", "onrl", "offrl", "onal", "offal"]

    if request.method == 'POST':
        command = request.form['command'].strip().lower()

        if command in valid_lamp_commands:
            mqtt_client.publish(mqtt_command_topic, command)
            status_message = f"Command '{command}' sent to Raspberry Pi."
        else:

            status_message = f"Invalid command."
        return render_template('lamp_commands.html', status_message=status_message)

    return render_template('lamp_commands.html', status_message=status_message)


@main_bp.route('/climate', methods=['GET', 'POST'])
def climate_func():
    print("Climate route accessed")
    if not session.get('user_verified'):
        return redirect(url_for('main_controller.profile_func'))

    global status_message

    if request.method == 'POST':
        command = request.form['command'].strip().lower()
        valid_commands = ["onclimate", "offclimate"]

        if command in valid_commands:
            mqtt_client.publish(mqtt_command_topic, command)
            status_message = f"Command '{command}' sent to Raspberry Pi."
        else:
            status_message = f"Invalid command."

    return render_template('climate.html',
                           status_message=status_message,
                           temperature=temperature,
                           humidity=humidity)


@main_bp.route('/climate-data', methods=['GET'])
def get_climate_data():
    if not session.get('user_verified'):
        return redirect(url_for('main_controller.profile_func'))
    temperature = current_app.config.get('TEMPERATURE', 'Not available')
    humidity = current_app.config.get('HUMIDITY', 'Not available')
    return jsonify({'temperature': temperature, 'humidity': humidity})


@main_bp.route('/room', methods=['GET', 'POST'])
def room_func():
    if not session.get('user_verified'):
        return redirect(url_for('main_controller.profile_func'))

    global status_message
    valid_rooms = ["room1", "room2"]
    valid_commands = ([f"on{room}" for room in valid_rooms] +
                      [f"off{room}" for room in valid_rooms] + ["onar", "offar"])

    if request.method == 'POST':
        command = request.form['command'].strip().lower()

        if command in valid_commands:
            mqtt_client.publish(mqtt_command_topic, command)
            status_message = f"Command '{command}' sent to Raspberry Pi."
        else:
            status_message = f"Invalid command."

        return render_template('room.html', status_message=status_message)

    return render_template('room.html', status_message=status_message)


@main_bp.route('/security', methods=['GET', 'POST'])
def security_func():
    if not session.get('user_verified'):
        return redirect(url_for('main_controller.profile_func'))

    global status_message
    valid_commands = ["onalert", "offalert"]

    if request.method == 'POST':
        command = request.form['command'].strip().lower()

        if command in valid_commands:
            mqtt_client.publish(mqtt_command_topic, command)
            status_message = f"Command '{command}' sent to Raspberry Pi."
        else:
            status_message = f"Invalid command."

        return render_template('security.html', status_message=status_message)

    return render_template('security.html', status_message=status_message)
