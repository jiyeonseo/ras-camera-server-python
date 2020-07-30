from flask import Flask
from flask import send_file
from camera import take
application = Flask(__name__)

@application.route("/")
def hello():
    filename = take()
    return send_file(filename, mimetype='image/gif')

if __name__ == "__main__":
    application.run(host='0.0.0.0')