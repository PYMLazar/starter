import os
from flask import Flask  
from flask_cors import CORS, cross_origin
from models import setup_db
#test
def create_app(test_config=None):

    app = Flask(__name__)
    app = create_app()
    setup_db(app)
    app.config.from_object('config')
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello" 
        if excited == 'true': greeting = greeting + "!!!!!"
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    return app

#app = create_app()

if __name__ == '__main__':
    app.run()