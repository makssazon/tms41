import datetime

from flask import request, render_template, redirect, url_for

from flask_todo.app import app
from flask_todo.models import TodoList


@app.route('/', methods=['POST', 'GET'])
def read_todo():
    if request.method == 'GET':
        if priority := request.args.get('priority'):
            data = TodoList.query. \
                filter_by(priority=priority). \
                order_by(TodoList.display_priority).all()
        else:
            data = TodoList.query.order_by(TodoList.display_priority).all()
        code = request.args.get('code') or 200
        return render_template('index.html', data=data,
                               priority=request.args.get('priority')), code
    else:
        data = TodoList.query.order_by(TodoList.id.desc()).first()
        display_priority = (data.id + 1) if data else 1
        link = TodoList(text=request.form['text'],
                        priority=request.form['priority'],
                        display_priority=display_priority,
                        date_create=datetime.datetime.now())
        link.save()
        return redirect(url_for('read_todo',
                                priority=request.args.get('priority')))


@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    link = TodoList.query.filter_by(id=id).first()
    link.delete()
    return redirect(url_for('read_todo',
                            priority=request.args.get('priority')))


@app.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    if request.method == 'GET':
        return render_template('update.html', id=id,
                               text=request.args.get('text'),
                               priority=request.args.get('priority'),
                               priority_old=request.args.get('priority_old'))
    else:
        link = TodoList.query. \
            filter_by(id=id).first()

        link.priority = request.form['priority']
        link.text = request.form['text']
        link.save()
        return redirect(url_for('read_todo',
                                priority=request.args.get('priority')))


@app.route('/up/<display>', methods=['POST'])
def up(display):
    link = TodoList.query.filter_by(display_priority=display).first()
    if priority := request.args.get('priority'):
        link_next = TodoList.query.filter_by(priority=priority). \
            filter(TodoList.display_priority < link.display_priority). \
            order_by(TodoList.display_priority.desc()).first()
    else:
        link_next = TodoList.query. \
            filter(TodoList.display_priority < link.display_priority). \
            order_by(TodoList.display_priority.desc()).first()
    if link_next:
        link.display_priority, link_next.display_priority = \
            link_next.display_priority, link.display_priority
        link.save()
        link_next.save()
        return redirect(url_for('read_todo',
                                priority=priority))
    return redirect(url_for('read_todo', code=400,
                            priority=priority))


@app.route('/down/<display>', methods=['POST'])
def down(display):
    link = TodoList.query.filter_by(display_priority=display).first()
    if priority := request.args.get('priority'):
        link_next = TodoList.query.filter_by(priority=priority). \
            filter(TodoList.display_priority > link.display_priority). \
            order_by(TodoList.display_priority).first()
    else:
        link_next = TodoList.query. \
            filter(TodoList.display_priority > link.display_priority). \
            order_by(TodoList.display_priority).first()
    if link_next:
        link.display_priority, link_next.display_priority = \
            link_next.display_priority, link.display_priority
        link.save()
        link_next.save()
        return redirect(url_for('read_todo',
                                priority=priority))
    return redirect(url_for('read_todo', code=400,
                            priority=priority))


@app.route('/done/<id>', methods=['POST'])
def done(id):
    link = TodoList.query.filter_by(id=id).first()
    link.done = not link.done
    link.save()
    return redirect(url_for('read_todo',
                            priority=request.args.get('priority')))
