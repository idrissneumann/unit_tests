from flask import Flask

def get_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app
