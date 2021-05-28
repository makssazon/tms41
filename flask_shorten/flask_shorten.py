import datetime

from flask import request, render_template, redirect

from flask_shorten.app import app
from flask_shorten.models import AllLinks


@app.route('/', methods=['POST', 'GET'])
def read_links():
    if request.method == 'GET':
        data_last = AllLinks.query.order_by(AllLinks.id.desc()).first()
        next_id = data_last.id + 1 if data_last else 1
        data = AllLinks.query.all()
        return render_template('index.html', data=data,
                               next_id=next_id, url=request.url)
    else:
        link1 = AllLinks.query.filter_by(origin_link=request.form['origin']). \
            first()
        link2 = AllLinks.query.filter_by(short_link=request.form['short']). \
            first()
        if link1:
            return render_template('success.html', result=1,
                                   link=link1, url=request.url), 400
        elif link2:
            return render_template('success.html', result=2,
                                   link=link2, url=request.url), 400
        else:
            if not request.form['short']:
                return render_template('success.html', result=5), 400
            else:
                link = AllLinks(origin_link=request.form['origin'],
                                short_link=request.form['short'],
                                date_create=datetime.datetime.now(),
                                counter=0)
                link.save()
                return render_template('success.html', result=3,
                                       link=link, url=request.url)


@app.route('/<string:end>')
def go_link(end=None):
    link = AllLinks.query.filter_by(short_link=end).first()
    if link:
        link.counter += 1
        link.save()
        return redirect(link.origin_link), 303
    else:
        return render_template('success.html', result=4, url=request.url), 404
