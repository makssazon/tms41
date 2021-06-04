# from unittest.mock import patch
#
# from flask import url_for
# from flask_testing import TestCase
# from _datetime import datetime
#
# from werkzeug.security import generate_password_hash
#
# from flask_todo.app import db
# from flask_todo.flask_todo import app
# from flask_todo.models import TodoList, User
#
# def login(self, username, password):
#     return self.client.post('/login', data=dict(
#         username=username,
#         password=password
#     ), follow_redirects=True)
#
# class ViewsTestCase(TestCase):
#     def create_app(self):
#         app.config['TESTING'] = True
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
#         return app
#
#     def setUp(self):
#         user = User(name='name', email='mail@a.a', hash_password=generate_password_hash('1234'))
#         db.session.add(user)
#         db.session.add(TodoList(text='text1',
#                                 priority=1,
#                                 display_priority=1,
#                                 date_create=datetime.now(),
#                                 user=user))
#         db.session.add(TodoList(text='text2',
#                                 priority=2,
#                                 display_priority=2,
#                                 date_create=datetime.now(),
#                                 user=user))
#
#         db.create_all()
#         db.session.commit()
#         self.client.post('/login', data=dict(
#             username='mail@a.a',
#             password='1234'
#         ), follow_redirects=False)
#         app.config['LOGIN_DISABLED'] = True
#         # self.client.post('/login', data={'email': 'mail@a.a', 'psw': '1234'})
#
#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()
#
#     def test_read_todo_if_if(self):
#         app.config['LOGIN_DISABLED'] = True
#
#         data = {'priority': 1}
#         response = self.client.get('/', query_string=data)
#         datatest = TodoList.query. \
#             filter_by(priority=data['priority']). \
#             order_by(TodoList.display_priority).all()
#         # self.assert200(response)
#         self.assertTemplateUsed('index.html')
#         self.assertContext('priority', str(data['priority']))
#         self.assertContext('data', datatest)
#
#     def test_read_todo_if_if_with_code(self):
#         data = {'priority': 1, 'code': 418}
#         response = self.client.get('/', query_string=data)
#         datatest = TodoList.query. \
#             filter_by(priority=data['priority']). \
#             order_by(TodoList.display_priority).all()
#         self.assertTemplateUsed('index.html')
#         self.assertContext('priority', str(data['priority']))
#         self.assertContext('data', datatest)
#         self.assertEqual(response.status_code, 418)
#
#     def test_read_todo_if_else(self):
#         response = self.client.get('/')
#         datatest = TodoList.query. \
#             order_by(TodoList.display_priority).all()
#         self.assert200(response)
#         self.assertTemplateUsed('index.html')
#         self.assertContext('priority', None)
#         self.assertContext('data', datatest)
#
#     def test_read_todo_if_else_with_code(self):
#         data = {'code': 418}
#         response = self.client.get('/', query_string=data)
#         datatest = TodoList.query. \
#             order_by(TodoList.display_priority).all()
#         self.assertEqual(response.status_code, 418)
#         self.assertTemplateUsed('index.html')
#         self.assertContext('priority', None)
#         self.assertContext('data', datatest)
#
#     def test_read_todo_else_if(self):
#         data = {'text': 'text1', 'priority': 1}
#         string = {'priority': 1}
#         response = self.client.post('/', data=data, query_string=string)
#         datatest = TodoList.query.all()
#         data_display = datatest[-1].display_priority
#         self.assertStatus(response, 302)
#         self.assertRedirects(response, url_for('read_todo', priority=1))
#         self.assertEqual(len(datatest), 3)
#         self.assertEqual(data_display, 3)
#
#     @patch('flask_todo.flask_todo.current_user')
#     def test_read_todo_else_else(self, mock_current_user):
#         TodoList.query.delete()
#         data = {'text': 'text1', 'priority': 1, 'user': mock_current_user}
#         string = {'priority': 1}
#         response = self.client.post('/', data=data, query_string=string)
#         datatest = TodoList.query.all()
#         data_display = datatest[0].display_priority
#         self.assertStatus(response, 302)
#         self.assertRedirects(response, url_for('read_todo', priority=1))
#         self.assertEqual(len(datatest), 1)
#         self.assertEqual(data_display, 1)
