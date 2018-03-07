import os
from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():

    token = request.form.get('token', None)

    if token == os.environ['VERIFICATION_TOKEN']:
        data = jsonify(text="You're a towel.",
                       response_type="in_channel")

        r = Response(data, status=200, mimetype='application/json')
        return r
    else:
        return Response("", status=401)

if __name__ == "__main__":
    app.run()
