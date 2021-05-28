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


db.init_app(app)
db.create_all()
