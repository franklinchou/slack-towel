from flask import Flask, Response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return Response("You're a towel.")

if __name__ == "__main__":
    app.run()
