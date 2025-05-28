from flask import Flask, request, jsonify
import time

app = Flask(__name__)


request_counts = {}


RATE_LIMIT = 5  # requests
TIME_WINDOW = 60  # seconds

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    client_ip = request.remote_addr
    current_time = time.time()

 
    if client_ip not in request_counts:
        request_counts[client_ip] = []

   
    request_counts[client_ip] = [timestamp for timestamp in request_counts[client_ip]
                                 if current_time - timestamp < TIME_WINDOW]

    if len(request_counts[client_ip]) >= RATE_LIMIT:
        request_counts[client_ip].append(current_time)
        return jsonify({'error': 'Rate limit exceeded. Try again later.',
                       'requests_in_window': len(request_counts[client_ip]) }), 429

  
    request_counts[client_ip].append(current_time)
    return jsonify({'message': 'Request accepted.',
                    'current_requests': len(request_counts[client_ip])}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
