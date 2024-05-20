from flask import Flask
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Chat Server is Running"

@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)

@socketio.on('current_page')
def handle_current_page(data):
    print(f"Current page: {data['page']}")
    emit('page_event', f"Page {data['page']} has been loaded", broadcast=True)

@socketio.on('user_activity')
def handle_user_activity(data):
    print(f"User activity: {data['activity']}")
    emit('activity_event', f"User {data['activity']}", broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
