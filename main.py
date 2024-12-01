import os
from flask import Flask, jsonify
from controllers.mainController import main_bp
from mqtt_client import set_flask_app

app = Flask(__name__, static_folder='static')
app.secret_key = os.urandom(24)
app.register_blueprint(main_bp)

set_flask_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
