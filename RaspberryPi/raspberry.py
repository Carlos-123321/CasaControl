# #This is the code meant to be put in the Raspberry Pi
# import paho.mqtt.client as mqtt
# import RPi.GPIO as GPIO
# import adafruit_dht
# import board
# import time
# import threading
# import json
#
# SENSOR = adafruit_dht.DHT11(board.D19)
#
# monitoring = False
#
# left_lamp_led = 17
# right_lamp_led = 18
# room_one_led = 27
# room_two_led = 22
# buzzer_pin = 26
#
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(left_lamp_led, GPIO.OUT)
# GPIO.setup(right_lamp_led, GPIO.OUT)
# GPIO.setup(room_one_led, GPIO.OUT)
# GPIO.setup(room_two_led, GPIO.OUT)
# GPIO.setup(buzzer_pin, GPIO.OUT)
#
# GPIO.output(left_lamp_led, GPIO.LOW)
# GPIO.output(right_lamp_led, GPIO.LOW)
# GPIO.output(room_one_led, GPIO.LOW)
# GPIO.output(room_two_led, GPIO.LOW)
#
# pwm = GPIO.PWM(buzzer_pin, 50)
# alert_on = False
#
#
# def turn_on_left_lamp():
#     GPIO.output(left_lamp_led, GPIO.HIGH)
#     print("Left Lamp is ON")
#
# def turn_off_left_lamp():
#     GPIO.output(left_lamp_led, GPIO.LOW)
#     print("Left Lamp is OFF")
#
# def turn_on_right_lamp():
#     GPIO.output(right_lamp_led, GPIO.HIGH)
#     print("Right Lamp is ON")
#
# def turn_off_right_lamp():
#     GPIO.output(right_lamp_led, GPIO.LOW)
#     print("Right Lamp is OFF")
#
# def turn_on_all_lamps():
#     GPIO.output(left_lamp_led, GPIO.HIGH)
#     GPIO.output(right_lamp_led, GPIO.HIGH)
#     print("ALL Lamps are ON")
#
# def turn_off_all_lamps():
#     GPIO.output(left_lamp_led, GPIO.LOW)
#     GPIO.output(right_lamp_led, GPIO.LOW)
#     print("ALL Lamps are OFF")
#
#
#
# def turn_on_room1():
#     GPIO.output(room_one_led, GPIO.HIGH)
#     print("Room 1 is ON")
#
# def turn_off_room1():
#     GPIO.output(room_one_led, GPIO.LOW)
#     print("Room 1 is OFF")
#
# def turn_on_room2():
#     GPIO.output(room_two_led, GPIO.HIGH)
#     print("Room 2 is ON")
#
# def turn_off_room2():
#     GPIO.output(room_two_led, GPIO.LOW)
#     print("Room 2 is OFF")
#
# def turn_on_all_rooms():
#     GPIO.output(room_one_led, GPIO.HIGH)
#     GPIO.output(room_two_led, GPIO.HIGH)
#     print("ALL Rooms are ON")
#
# def turn_off_all_rooms():
#     GPIO.output(room_one_led, GPIO.LOW)
#     GPIO.output(room_two_led, GPIO.LOW)
#     print("ALL Rooms are OFF")
#
#
#
# def alert_logic():
#     global alert_on
#     pwm.start(50)
#     print("Buzzer is ON")
#
#     try:
#         while alert_on:
#             print("Cycle 1: Slow sweep")
#             for GPFrequency in range(100, 500, 10):
#                 if not alert_on:
#                     pwm.stop()
#                     return
#                 pwm.ChangeFrequency(GPFrequency)
#                 time.sleep(0.05)
#     except KeyboardInterrupt:
#         pwm.stop()
#     finally:
#         pwm.stop()
#
# def turn_on_alert():
#     global alert_on
#     if not alert_on:
#         alert_on = True
#         alert_thread = threading.Thread(target=alert_logic, daemon=True)
#         alert_thread.start()
#
# def turn_off_alert():
#     global alert_on
#     if alert_on:
#         alert_on = False
#         print("Buzzer is OFF")
#
#
#
# def start_climate_monitoring():
#
#     global monitoring
#     if not monitoring:
#         monitoring = True
#         climate_thread = threading.Thread(target=monitor_climate, daemon=True)
#         climate_thread.start()
#         print("Climate monitoring started.")
#     else:
#         print("Climate monitoring is already running.")
#
# def stop_climate_monitoring():
#
#     global monitoring
#     if monitoring:
#         monitoring = False
#         print("Climate monitoring stopped.")
#     else:
#         print("Climate monitoring is not running.")
#
#
# def monitor_climate():
#
#     print("Monitoring climate... Press 'offclimate' to stop.")
#     while monitoring:
#         try:
#             temperature = SENSOR.temperature
#             humidity = SENSOR.humidity
#             if humidity is not None and temperature is not None:
#                 print(f"Temperature: {temperature:.1f}C, Humidity: {humidity:.1f}%")
#
#                 client.publish(CLIMATE_TOPIC + "/temperature", json.dumps({"temperature": temperature}))
#                 client.publish(CLIMATE_TOPIC + "/humidity", json.dumps({"humidity": humidity}))
#
#             else:
#                 print("Failed to retrieve sensor data. Retrying...")
#             time.sleep(2)
#         except RuntimeError as error:
#             print(f"Sensor error: {error}")
#             time.sleep(2)
#     print("Exiting climate monitoring loop.")
#
#
# BROKER = "rpi2024"
# PORT = 1883
# COMMAND_TOPIC = "home/commands"
# STATUS_TOPIC = "home/status"
# CLIMATE_TOPIC = "home/climate"
#
#
# def on_connect(client, userdata, flags, rc):
#     if rc == 0:
#         print("Connected successfully")
#     else:
#         print(f"Connection failed with code {rc}")
#     client.subscribe(COMMAND_TOPIC)
#
# def on_message(client, userdata, msg):
#     command = msg.payload.decode().strip().lower()
#     print(f"Received command: {command}")
#
#
#     if command == "onll":
#         turn_on_left_lamp()
#         client.publish(STATUS_TOPIC, "I am now doing "  + command)
#
#     elif command == "offll":
#         turn_off_left_lamp()
#         client.publish(STATUS_TOPIC, "I am now doing " + command)
#
#     elif command == "onrl":
#         turn_on_right_lamp()
#         client.publish(STATUS_TOPIC, "I am now doing "  + command)
#
#     elif command == "offrl":
#         turn_off_right_lamp()
#         client.publish(STATUS_TOPIC, "I am now doing "  + command)
#
#     elif command == "onal":
#         turn_on_all_lamps()
#         client.publish(STATUS_TOPIC, "I am now doing "  + command)
#
#     elif command == "offal":
#         turn_off_all_lamps()
#         client.publish(STATUS_TOPIC, "I am now doing "  + command)
#
#
#
#     elif command == "onroom1":
#         turn_on_room1()
#         client.publish(STATUS_TOPIC, "I am now doing "  + command)
#
#     elif command == "offroom1":
#         turn_off_room1()
#         client.publish(STATUS_TOPIC, "I am now doing "  + command)
#
#
#     elif command == "onroom2":
#         turn_on_room2()
#         client.publish(STATUS_TOPIC, "I am now doing "  + command)
#
#     elif command == "offroom2":
#         turn_off_room2()
#
#         client.publish(STATUS_TOPIC, "I am now doing "  + command)
#
#     elif command == "onar":
#         turn_on_all_rooms()
#         client.publish(STATUS_TOPIC, "I am now doing "  + command)
#
#     elif command == "offar":
#         turn_off_all_rooms()
#         client.publish(STATUS_TOPIC, "I am now doing "  + command)
#
#
#
#
#     elif command == "onalert":
#         turn_on_alert()
#         print("Alert is ON")
#         client.publish(STATUS_TOPIC, "I am now doing " + command)
#
#     elif command == "offalert":
#         turn_off_alert()
#         print("Alert is OFF")
#         client.publish(STATUS_TOPIC, "I am now doing " + command)
#
#
#
#
#     elif command == "onclimate":
#         start_climate_monitoring()
#         client.publish(STATUS_TOPIC, "Climate monitoring started.")
#
#     elif command == "offclimate":
#         stop_climate_monitoring()
#         client.publish(STATUS_TOPIC, "Climate monitoring stopped.")
#
#
#
#     else:
#         print("Unknown command received")
#         client.publish(STATUS_TOPIC, f"Unknown command: {command}")
#
#
# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message
#
# client.connect(BROKER, PORT, 60)
#
# try:
#     client.loop_forever()
# except KeyboardInterrupt:
#     print("Exiting...")
#     GPIO.cleanup()
#     client.disconnect()
