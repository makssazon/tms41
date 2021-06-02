import datetime

from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash

from flask_todo.app import app
from flask_todo.forms import LoginForm, RegisterForm
from flask_todo.models import TodoList, User
from flask_todo.utils.exeptions import NoUserOrPSW
from flask_todo.utils.functions import get_user_by_email_and_check_psw, check_user_name_and_email, get_todo_for_user, \
    find_next_display_priority_for_user


@app.route('/', methods=['POST', 'GET'])
@login_required
def read_todo():
    if request.method == 'GET':
        data = get_todo_for_user(current_user.id, request.args.get('priority'))
        code = request.args.get('code') or 200
        return render_template('index.html', data=data,
                               priority=request.args.get('priority'), user=current_user), code
    else:
        display_priority = find_next_display_priority_for_user(current_user.id)
        link = TodoList(text=request.form['text'],
                        priority=request.form['priority'],
                        display_priority=display_priority,
                        date_create=datetime.datetime.now(),
                        user=current_user)
        link.save()
        return redirect(url_for('read_todo',
                                priority=request.args.get('priority'),
                                user=current_user))


@app.route('/delete/<id>', methods=['POST'])
@login_required
def delete(id):
    link = TodoList.query.filter_by(id=id).first()
    link.delete()
    return redirect(url_for('read_todo',
                            priority=request.args.get('priority'), user=current_user))


@app.route('/update/<id>', methods=['POST', 'GET'])
@login_required
def update(id):
    if request.method == 'GET':
        return render_template('update.html', id=id,
                               text=request.args.get('text'),
                               priority=request.args.get('priority'),
                               priority_old=request.args.get('priority_old'),
                               user=current_user)
    else:
        link = TodoList.query. \
            filter_by(id=id).first()

        link.priority = request.form['priority']
        link.text = request.form['text']
        link.save()
        return redirect(url_for('read_todo',
                                priority=request.args.get('priority'),
                                user=current_user))


@app.route('/up/<display>', methods=['POST'])
@login_required
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
                                priority=priority, user=current_user))
    return redirect(url_for('read_todo', code=400,
                            priority=priority, user=current_user))


@app.route('/down/<display>', methods=['POST'])
@login_required
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
                                priority=priority, user=current_user))
    return redirect(url_for('read_todo', code=400,
                            priority=priority, user=current_user))


@app.route('/done/<id>', methods=['POST'])
@login_required
def done(id):
    link = TodoList.query.filter_by(id=id).first()
    link.done = not link.done
    link.save()
    return redirect(url_for('read_todo',
                            priority=request.args.get('priority'), user=current_user))


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form, user=current_user)
    if form.validate_on_submit():  # check forms errors
        email = form.email.data
        psw = form.psw.data
        try:
            user = get_user_by_email_and_check_psw(email, psw)
        except NoUserOrPSW:
            flash('error with email or psw', category='error')
            return render_template('login.html', form=form, user=current_user), 400
        login_user(user, remember=form.remember.data)
        return redirect(url_for('read_todo', user=current_user))
    return render_template('login.html', form=form, user=current_user), 400


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form, user=current_user)
    if form.validate_on_submit():
        name = form.username.data
        email = form.email.data
        if check_user_name_and_email(name, email):
            flash('user with email or name is used', category='error')
            return render_template('register.html', form=form, user=current_user), 400
        psw = generate_password_hash(form.psw.data)
        user = User(name=name, email=email, hash_password=psw)
        user.save()
        flash(f'user {name} was created', category='success')
        return redirect(url_for('login', user=current_user))
    return render_template('register.html', form=form, user=current_user), 400


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('read_todo', user=current_user))
