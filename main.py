import os

from flask import Flask, session
from controllers.mainController import main_bp

app = Flask(__name__, static_folder='static')
app.secret_key = os.urandom(24)
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
