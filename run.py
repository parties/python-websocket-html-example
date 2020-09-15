from app import app, socketio

if __name__ == "__main__":
    print('--- http://localhost:5000 ---')
    socketio.run(app)
