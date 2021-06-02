from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .app import db, app


class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class TodoList(BaseModel):
    id = db.Column('id', db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    priority = db.Column(db.Integer)
    display_priority = db.Column(db.Integer)
    date_create = db.Column(db.DateTime)
    done = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=True)
    user = relationship(
        'User', foreign_keys='TodoList.user_id', backref='todo'
    )


class User(UserMixin, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    hash_password = db.Column(db.String, nullable=False, unique=True)
    created_on = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'{self.id} {self.name}'


db.init_app(app)
db.create_all()
