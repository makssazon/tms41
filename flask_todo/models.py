from .app import db, app


class TodoList(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    priority = db.Column(db.Integer)
    display_priority = db.Column(db.Integer)
    date_create = db.Column(db.DateTime)
    done = db.Column(db.Boolean, default=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


db.init_app(app)
db.create_all()
