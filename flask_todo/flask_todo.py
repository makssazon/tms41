import datetime

from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='../templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flasktodo.db'
db = SQLAlchemy(app)


class TodoList(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    priority = db.Column(db.Integer)
    display_priority = db.Column(db.Integer)
    date_create = db.Column(db.DateTime)
    done = db.Column(db.Boolean, default=False)


db.init_app(app)
db.create_all()


@app.route('/', methods=['POST', 'GET'])
def read_todo():
    if request.method == 'GET':
        if request.args.get('priority'):
            data = TodoList.query. \
                filter_by(priority=request.args.get('priority')). \
                order_by(TodoList.display_priority).all()
        else:
            data = TodoList.query.order_by(TodoList.display_priority).all()
        code = 200
        if request.args.get('code'):
            code = request.args.get('code')
        return render_template('index.html', data=data,
                               priority=request.args.get('priority')), code
    else:
        data = TodoList.query.all()
        if data:
            display_priority = list(data)[-1].id + 1
        else:
            display_priority = 1
        link = TodoList(text=request.form['text'],
                        priority=request.form['priority'],
                        display_priority=display_priority,
                        date_create=datetime.datetime.now())
        db.session.add(link)
        db.session.commit()
        return redirect(url_for('read_todo',
                                priority=request.args.get('priority')))


@app.route('/delete')
def delete():
    TodoList.query.filter_by(id=request.args.get('id')).delete()
    db.session.commit()
    return redirect(url_for('read_todo',
                            priority=request.args.get('priority')))


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'GET':
        return render_template('update.html', id=request.args.get('id'),
                               priority=request.args.get('priority'))
    else:
        link = TodoList.query.\
            filter_by(id=request.args.get('id')).first()
        link.text = request.form['text']
        link.priority = request.form['priority']
        db.session.commit()
        return redirect(url_for('read_todo',
                                priority=request.args.get('priority')))


@app.route('/up')
def up():
    display = request.args.get('display')
    link = TodoList.query.filter_by(display_priority=display).first()
    all_links = TodoList.query.order_by(TodoList.display_priority).all()
    index = all_links.index(link)
    if index == 0:
        return redirect(url_for('read_todo', code=400,
                                priority=request.args.get('priority')))
    link2 = all_links[index - 1]
    link.display_priority, link2.display_priority = \
        link2.display_priority, link.display_priority
    db.session.commit()
    return redirect(url_for('read_todo',
                            priority=request.args.get('priority')))


@app.route('/down')
def down():
    display = request.args.get('display')
    link = TodoList.query.filter_by(display_priority=display).first()
    all_links = TodoList.query.order_by(TodoList.display_priority).all()
    index = all_links.index(link)
    if index + 1 == len(all_links):
        return redirect(url_for('read_todo', code=400,
                                priority=request.args.get('priority')))
    link2 = all_links[index + 1]
    link.display_priority, link2.display_priority = \
        link2.display_priority, link.display_priority
    db.session.commit()
    return redirect(url_for('read_todo',
                            priority=request.args.get('priority')))


@app.route('/done')
def done():
    link = TodoList.query.filter_by(id=request.args.get('id')).first()
    link.done = not link.done
    db.session.commit()
    return redirect(url_for('read_todo',
                            priority=request.args.get('priority')))


if __name__ == '__main__':
    app.run()
