from flask import url_for
from flask_testing import TestCase
from _datetime import datetime

from flask_todo.flask_todo import app, db
from flask_todo.models import TodoList


class ViewsTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.session.add(TodoList(text='text1',
                                priority=1,
                                display_priority=1,
                                date_create=datetime.now(),
                                done=False))
        db.session.add(TodoList(text='text2',
                                priority=2,
                                display_priority=2,
                                date_create=datetime.now(),
                                done=False))
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_read_todo_if_if(self):
        data = {'priority': 1}
        response = self.client.get('/', query_string=data)
        datatest = TodoList.query. \
            filter_by(priority=data['priority']). \
            order_by(TodoList.display_priority).all()
        self.assert200(response)
        self.assertTemplateUsed('index.html')
        self.assertContext('priority', str(data['priority']))
        self.assertContext('data', datatest)

    def test_read_todo_if_if_with_code(self):
        data = {'priority': 1, 'code': 418}
        response = self.client.get('/', query_string=data)
        datatest = TodoList.query. \
            filter_by(priority=data['priority']). \
            order_by(TodoList.display_priority).all()
        self.assertTemplateUsed('index.html')
        self.assertContext('priority', str(data['priority']))
        self.assertContext('data', datatest)
        self.assertEqual(response.status_code, 418)

    def test_read_todo_if_else(self):
        response = self.client.get('/')
        datatest = TodoList.query. \
            order_by(TodoList.display_priority).all()
        self.assert200(response)
        self.assertTemplateUsed('index.html')
        self.assertContext('priority', None)
        self.assertContext('data', datatest)

    def test_read_todo_if_else_with_code(self):
        data = {'code': 418}
        response = self.client.get('/', query_string=data)
        datatest = TodoList.query. \
            order_by(TodoList.display_priority).all()
        self.assertEqual(response.status_code, 418)
        self.assertTemplateUsed('index.html')
        self.assertContext('priority', None)
        self.assertContext('data', datatest)

    def test_read_todo_else_if(self):
        data = {'text': 'text1', 'priority': 1}
        string = {'priority': 1}
        response = self.client.post('/', data=data, query_string=string)
        datatest = TodoList.query.all()
        data_display = datatest[-1].display_priority
        self.assertStatus(response, 302)
        self.assertRedirects(response, url_for('read_todo', priority=1))
        self.assertEqual(len(datatest), 3)
        self.assertEqual(data_display, 3)

    def test_read_todo_else_else(self):
        TodoList.query.delete()
        data = {'text': 'text1', 'priority': 1}
        string = {'priority': 1}
        response = self.client.post('/', data=data, query_string=string)
        datatest = TodoList.query.all()
        data_display = datatest[0].display_priority
        self.assertStatus(response, 302)
        self.assertRedirects(response, url_for('read_todo', priority=1))
        self.assertEqual(len(datatest), 1)
        self.assertEqual(data_display, 1)

    def test_delete(self):
        response = self.client.post('/delete/1')
        datatest = TodoList.query.all()
        self.assertStatus(response, 302)
        self.assertRedirects(response, url_for('read_todo'))
        self.assertEqual(len(datatest), 1)

    def test_update_if(self):
        string = {'priority': 1, 'text': 'text1', 'priority_old': 1}
        response = self.client.get('/update/1', query_string=string)
        self.assert200(response)
        self.assertTemplateUsed('update.html')
        self.assertContext('text', string['text'])
        self.assertContext('priority', str(1))
        self.assertContext('priority_old', str(1))

    def test_update_else(self):
        data = {'text': 'testupdate', 'priority': 3}
        string = {'priority': 1}
        response = self.client.post('/update/1',
                                    data=data, query_string=string)
        datatest = TodoList.query.first()
        self.assertEqual(datatest.text, 'testupdate')
        self.assertEqual(datatest.priority, 3)
        self.assertStatus(response, 302)
        self.assertRedirects(response, url_for('read_todo', priority=1))
