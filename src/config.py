import os


def set_app_configs(app):
    DB_USERNAME = 'postgres'
    DB_PASSWORD = '123456'
    # DB_HOST = 'localhost'
    # DB_PORT = 5431
    DB_HOST = 'db'
    DB_PORT = 5432
    DATABASE_NAME = 'api_graphql'
    DB_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    return app
