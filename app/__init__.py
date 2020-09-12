from flask import Flask
from flask_socketio import SocketIO

# initialize flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

# wrap app in socketio
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
    print(f'received message: {message}')

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

from app import views
