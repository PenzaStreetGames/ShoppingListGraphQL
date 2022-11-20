from flask_sqlalchemy import SQLAlchemy
from app import get_app
from api import models

app = get_app()
db = SQLAlchemy()
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        models.create_all()
    app.run(host='0.0.0.0', port=8080, debug=True)
