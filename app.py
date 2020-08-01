from flask import Flask
from flask import send_file
import os

from camera import take
from storage import upload as azure_upload

application = Flask(__name__)

@application.route("/")
def main():
    local_path = "."
    local_file_name = take()
    upload_file_path = os.path.join(local_path, local_file_name)
    return azure_upload(upload_file_path, local_file_name)

if __name__ == "__main__":
    application.run(host='0.0.0.0')