from flask import Flask

_app = Flask(__name__)

@_app.route('/myapp/', methods=['GET'])
def hello_world():
    return "Hello World", 200


if __name__ == '__main__':
    _app.run(host = '0.0.0.0', port = 64500)

