from flask import Flask, render_template
from flask_socketio import SocketIO
from textblob import TextBlob

app = Flask(__name__)
socketio = SocketIO(app, async_mode='threading')  # or 'eventlet' or 'gevent'

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    message = data['message']
    sentiment = get_sentiment(message)
    emit_message = {'message': message, 'sentiment': sentiment}
    socketio.emit('message', emit_message)

def get_sentiment(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity

    if sentiment > 0:
        return 'positive'
    elif sentiment < 0:
        return 'negative'
    else:
        return 'neutral'

if __name__ == '__main__':
    socketio.run(app, debug=True)
