import datetime
import socket
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/details', methods=['GET'])
def details():
    return jsonify({
      'time': datetime.datetime.now().strftime("%H:%M:%S on %Y-%m-%d"),
      'hostname': socket.gethostname()
      })
  
@app.route('/api/v1/health', methods=['GET'])
def health():
    return jsonify({"status": "up"}, 200)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
    