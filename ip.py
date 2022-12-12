from flask import Flask, request
from bot import *
from env import D_TOKEN

app = Flask(__name__)
ip_address = None

@app.route('/')
def home():
    ip_address = request.remote_addr
    client.run(D_TOKEN)
    return f"{ip_address}"

if __name__ == '__main__':
    app.run(debug=True)