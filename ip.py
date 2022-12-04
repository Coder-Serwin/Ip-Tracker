from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    ip_address = request.remote_addr
    return f"<h1> Your Ip address is {ip_address}"


if __name__ == '__main__':
    app.run(debug=True, port=8080)