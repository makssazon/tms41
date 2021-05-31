from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash

from flask_shorten.app import db, app


class AllLinks(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    origin_link = db.Column(db.String(100))
    short_link = db.Column(db.String(100))
    date_create = db.Column(db.DateTime)
    counter = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    hash_password = db.Column(db.String, nullable=False, unique=True)
    created_on = db.Column(db.DateTime, default=datetime.now)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.hash_password, password)

    def __repr__(self):
        return f'{self.id} {self.name}'


db.init_app(app)
db.create_all()
