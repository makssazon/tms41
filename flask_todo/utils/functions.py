from sqlalchemy import or_
from werkzeug.security import check_password_hash

from flask_todo.models import User, TodoList
from flask_todo.utils.exeptions import NoUserOrPSW


def get_user_by_email_and_check_psw(email, psw) -> User:
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.hash_password, psw):
        return user
    raise NoUserOrPSW


def check_user_name_and_email(name, email) -> bool:
    return bool(User.query.filter(or_(User.name == name, User.email == email)).first())


def get_todo_for_user(user_id, priority):
    if priority:
        data = TodoList.query.filter_by(user_id=user_id). \
            filter_by(priority=priority). \
            order_by(TodoList.display_priority).all()
    else:
        data = TodoList.query.filter(TodoList.user_id == user_id). \
            order_by(TodoList.display_priority).all()
    return data


def find_next_display_priority_for_user(user_id) -> int:
    data = TodoList.query.filter_by(user_id=user_id).order_by(TodoList.id.desc()).first()
    display_priority = (data.id + 1) if data else 1
    return display_priority
