from config import db
from models.model import Model

def insert_user(name, email):
    new_user = Model(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

def fetch_all_users():
    return Model.query.all()

def get_by_id(user_id):
    return Model.query.get(user_id)

def delete_user(user_id):
    user = get_by_id(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False