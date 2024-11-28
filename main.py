from flask import Flask
from controllers.mainController import main_bp

app = Flask(__name__, static_folder='static')
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
