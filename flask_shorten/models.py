from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from flask_shorten.app import db, app


class AllLinks(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    origin_link = db.Column(db.String(100))
    short_link = db.Column(db.String(100))
    date_create = db.Column(db.DateTime)
    counter = db.Column(db.Integer)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=True)
    user = relationship(
        'User', foreign_keys='AllLinks.user_id', backref='links'
    )

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

    def __repr__(self):
        return f'{self.id} {self.name}'


db.init_app(app)
db.create_all()
