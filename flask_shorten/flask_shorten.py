import datetime

from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='../templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskshorten.db'
db = SQLAlchemy(app)


class AllLinks(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    origin_link = db.Column(db.String(100))
    short_link = db.Column(db.String(100))
    date_create = db.Column(db.DateTime)
    counter = db.Column(db.Integer)


db.init_app(app)
db.create_all()


@app.route('/', methods=['POST', 'GET'])
def read_links():
    if request.method == 'GET':
        data = AllLinks.query.all()
        if data:
            next_id = list(data)[-1].id + 1
        else:
            next_id = 1
        return render_template('index.html', data=data,
                               next_id=next_id, url=request.url)
    else:
        link1 = AllLinks.query.filter_by(origin_link=request.form['origin']).\
            first()
        link2 = AllLinks.query.filter_by(short_link=request.form['short']).\
            first()
        if link1:
            return render_template('success.html', result=1,
                                   link=link1, url=request.url)
        elif link2:
            return render_template('success.html', result=2,
                                   link=link2, url=request.url)
        else:
            link = AllLinks(origin_link=request.form['origin'],
                            short_link=request.form['short'],
                            date_create=datetime.datetime.now(),
                            counter=0)
            db.session.add(link)
            db.session.commit()
            return render_template('success.html', result=3,
                                   link=link, url=request.url)


@app.route('/<string:end>')
def go_link(end=None):
    link = AllLinks.query.filter_by(short_link=end).first()
    if link:
        link.counter += 1
        db.session.commit()
        return redirect(link.origin_link)
    else:
        return render_template('success.html', result=4, url=request.url)


if __name__ == '__main__':
    app.run()
