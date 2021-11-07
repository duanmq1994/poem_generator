from os import environ
from Generator import app

if __name__ == '__main__':
    HOST = '0.0.0.0'
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)