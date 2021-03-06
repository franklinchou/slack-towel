import os
from flask import Flask, Response, request, jsonify

app = Flask(__name__)

DEFAULT='application/json'

@app.route('/health', methods=['GET'])
def health():
    if os.environ['DEPLOY_TARGET'] == 'dev':
        return Response("", status=200, mimetype=DEFAULT)

@app.route('/', methods=['POST'])
def main() -> Response:

    token = request.form.get('token', None)
    channel = request.form.get('channel_id', None)

    if token == os.environ['VERIFICATION_TOKEN']:
        data = jsonify(text="You're a towel.",
                       token=os.environ['VERIFICATION_TOKEN'],
                       response_type="in_channel",
                       channel=channel,
                       mimetype=DEFAULT)
        data.status_code = 200
        return data
    else:
        return Response("", status=401, mimetype=DEFAULT)

if __name__ == "__main__":
    app.run()
