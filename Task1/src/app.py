from flask import Flask, request, jsonify
import redis
import os

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

RATE_LIMIT = 5
TIME_WINDOW = 60

@app.route('/submit', methods=['GET'])
def submit():
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    key = f"rate_limit:{client_ip}"

    try:
        count = redis_client.incr(key)
        if count == 1:
            redis_client.expire(key, TIME_WINDOW)

        if count > RATE_LIMIT:
            return jsonify({'error': 'Rate limit exceeded. Try again later.'}), 429

        return jsonify({'message': 'Request accepted.', 'requests_in_window': count}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)