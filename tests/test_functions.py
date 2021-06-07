from datetime import datetime

from flask_testing import TestCase
from werkzeug.security import generate_password_hash

from flask_todo.app import db
from flask_todo.flask_todo import app
from flask_todo.models import TodoList, User
from flask_todo.utils.exeptions import NoLink, NoUserOrPSW
from flask_todo.utils.functions import get_user_by_email_and_check_psw, check_user_name_and_email, get_todo_for_user, \
    find_next_display_priority_for_user, get_up_link, get_down_link


class TestViews(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        return app

    def setUp(self):
        user = User(name='name',
                    email='mail@a.a',
                    hash_password=generate_password_hash('1234'))
        db.session.add(user)
        db.session.add(TodoList(text='text1',
                                priority=1,
                                display_priority=1,
                                date_create=datetime.now(),
                                user=user))
        db.session.add(TodoList(text='text2',
                                priority=2,
                                display_priority=2,
                                date_create=datetime.now(),
                                user=user))

        db.create_all()
        db.session.commit()
        app.config['LOGIN_DISABLED'] = True

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_user_by_email_and_check_psw(self):
        result = get_user_by_email_and_check_psw('mail@a.a', '1234')
        datatest = User.query.filter_by(email='mail@a.a').first()
        self.assertEqual(result, datatest)

    def test_get_user_by_email_and_check_psw_raise(self):
        self.assertRaises(NoUserOrPSW, get_user_by_email_and_check_psw, 'mail@a.', '1234')

    def test_get_user_by_email_and_check_psw_raise_no_psw(self):
        self.assertRaises(NoUserOrPSW, get_user_by_email_and_check_psw, 'mail@a.a', '11234')

    def test_check_user_name_and_email_true(self):
        result = check_user_name_and_email('name', 'mail@a.a')
        self.assertTrue(result)

    def test_check_user_name_and_email_true_name(self):
        result = check_user_name_and_email('name', '1mail@a.a')
        self.assertTrue(result)

    def test_check_user_name_and_email_true_mail(self):
        result = check_user_name_and_email('1name', 'mail@a.a')
        self.assertTrue(result)

    def test_check_user_name_and_email_false(self):
        result = check_user_name_and_email('name1', '1mail@a.a')
        self.assertFalse(result)

    def test_get_todo_for_user_if(self):
        result = get_todo_for_user(1, 1)
        datatest = TodoList.query.first()
        self.assertEqual(result, [datatest])

    def test_get_todo_for_user_else(self):
        result = get_todo_for_user(1, None)
        datatest = TodoList.query.all()
        self.assertEqual(result, datatest)

    def test_find_next_display_priority_for_user(self):
        result = find_next_display_priority_for_user()
        self.assertEqual(result, 3)

    def test_find_next_display_priority_for_user_without_data(self):
        TodoList.query.delete()
        result = find_next_display_priority_for_user()
        self.assertEqual(result, 1)

    def test_get_up_link(self):
        link = TodoList.query.filter_by(display_priority=2).first()
        priority = None
        user = User.query.first()
        result = get_up_link(link, priority, user)
        testdata = TodoList.query.filter_by(display_priority=1).first()
        self.assertEqual(result, testdata)

    def test_get_up_link_raise(self):
        link = TodoList.query.filter_by(display_priority=1).first()
        priority = None
        user = User.query.first()
        self.assertRaises(NoLink, get_up_link, link, priority, user)

    def test_get_down_link(self):
        link = TodoList.query.filter_by(display_priority=1).first()
        priority = None
        user = User.query.first()
        result = get_down_link(link, priority, user)
        testdata = TodoList.query.filter_by(display_priority=2).first()
        self.assertEqual(result, testdata)

    def test_get_down_link_raise(self):
        link = TodoList.query.filter_by(display_priority=2).first()
        priority = None
        user = User.query.first()
        self.assertRaises(NoLink, get_down_link, link, priority, user)
