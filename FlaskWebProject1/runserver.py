"""
This script runs the FlaskWebProject1 application using a development server.

指令 (工具 > Python > Python環境 > 在PowerShell中開啟:
python runserver.py

localhost測試工具
ngrok:
https://dashboard.ngrok.com/get-started

"""

from os import environ
from FlaskWebProject1 import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
