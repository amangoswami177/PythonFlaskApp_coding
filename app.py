# app.py

from flask import Flask 
from urllib.parse import quote 

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'wow ci-cd pipeline done and class 7'

    return app
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
