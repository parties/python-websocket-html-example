import time
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

@socketio.on('save:json')
def save_json(json):
    print(f'got json: {str(json)}')
    timers = [1, 2, 2.5, 3.5, 1.5, 3]
    messages = [
        'saving data...',
        'still saving data...',
        'taking a nep...',
        'dreaming...',
        'wrapping up...',
        'reticulating splines...'
    ]
    total = len(timers)
    for index in range(total):
        socketio.emit('progress', f'{index + 1}/{total} - {messages[index]}')
        time.sleep(timers[index])
    socketio.emit('progress', 'done')

@socketio.on('echo')
def echo(message):
    # socketio.send(message)
    socketio.emit('echo', message)

from app import views
