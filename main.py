from flask import Flask, request, jsonify
from converter import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def download():
    data = download_audio(request.args.get('vid'))
    return jsonify(data)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8888")
    )