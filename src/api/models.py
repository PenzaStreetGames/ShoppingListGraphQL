from main import db


class ShoppingListItem(db.Model):
    uid = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    quantity = db.Column(db.Integer)
    completed = db.Column(db.Boolean)
    user_uid = db.Column(db.String)

    def to_dict(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "quantity": self.quantity,
            "completed": self.completed,
            "user_uid": self.user_uid
        }


def create_all():
    db.create_all()
