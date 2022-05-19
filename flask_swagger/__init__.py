from flask import Flask

def init_app():
    app = Flask(__name__)
    from flask_swagger.dbconfig import swag
    app.register_blueprint(swag)
    return app
