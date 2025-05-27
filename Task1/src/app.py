from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# In-memory store for request timestamps per IP
request_counts = {}

# Rate limit configuration
RATE_LIMIT = 5  # requests
TIME_WINDOW = 60  # seconds

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    client_ip = request.remote_addr
    current_time = time.time()

    # Initialize request history for new IPs
    if client_ip not in request_counts:
        request_counts[client_ip] = []

    # Filter out timestamps older than TIME_WINDOW
    request_counts[client_ip] = [timestamp for timestamp in request_counts[client_ip]
                                 if current_time - timestamp < TIME_WINDOW]

    if len(request_counts[client_ip]) >= RATE_LIMIT:
        return jsonify({'error': 'Rate limit exceeded. Try again later.'}), 429

    # Record the current request
    request_counts[client_ip].append(current_time)
    return jsonify({'message': 'Request accepted.'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
