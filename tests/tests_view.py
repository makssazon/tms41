from datetime import datetime
from unittest.mock import patch, MagicMock

from flask import url_for
from flask_testing import TestCase
from werkzeug.security import generate_password_hash

from flask_todo.app import db
from flask_todo.flask_todo import app
from flask_todo.models import TodoList, User
from flask_todo.utils.exeptions import NoLink, NoUserOrPSW


class TestViews(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        return app

    def setUp(self):
        user = User(name='name', email='mail@a.a', hash_password=generate_password_hash('1234'))
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

    @patch('flask_todo.flask_todo.get_todo_for_user')
    @patch('flask_todo.flask_todo.current_user')
    def test_read_get_for_user(self, mock_current_user,
                               mock_get_todo_for_user):
        app.config['LOGIN_DISABLED'] = True
        mock1, mock2 = MagicMock(), MagicMock()
        mock_get_todo_for_user.return_value = [mock1, mock2]
        response = self.client.get('/')
        mock_get_todo_for_user.assert_called_once_with(mock_current_user.id, None)
        self.assert200(response)
        self.assertEqual(self.get_context_variable('data'), [mock1, mock2])
        self.assertEqual(self.get_context_variable('user'), mock_current_user)
        self.assertEqual(self.get_context_variable('priority'), None)

    @patch('flask_todo.flask_todo.get_todo_for_user')
    @patch('flask_todo.flask_todo.current_user')
    def test_read_get_for_user_with_priority_and_code(self, mock_current_user,
                                                      mock_get_todo_for_user):
        app.config['LOGIN_DISABLED'] = True
        mock1, mock2 = MagicMock(), MagicMock()
        mock_get_todo_for_user.return_value = (mock1, mock2)
        response = self.client.get('/', query_string={'priority': '1', 'code': 400})
        mock_get_todo_for_user.assert_called_once_with(mock_current_user.id, '1')
        self.assert400(response)
        self.assertEqual(self.get_context_variable('data'), (mock1, mock2))
        self.assertEqual(self.get_context_variable('user'), mock_current_user)
        self.assertEqual(self.get_context_variable('priority'), '1')

    @patch('flask_todo.flask_todo.find_next_display_priority_for_user')
    @patch('flask_todo.flask_todo.current_user')
    @patch('flask_todo.flask_todo.TodoList')
    @patch('flask_todo.flask_todo.datetime')
    def test_read_post(self, mock_date, mock_TodoList, mock_current_user,
                       mock_find_next_display_priority_for_user):
        app.config['LOGIN_DISABLED'] = True
        mock_find_next_display_priority_for_user.return_value = 1
        # mock_date.datetime.now.return_value = 'date'
        response = self.client.post('/', data={'text': 'text',
                                               'priority': 'priority'},
                                    query_string={'priority': 1})

        mock_TodoList.assert_called_once_with(text='text',
                                              priority='priority',
                                              display_priority=1,
                                              date_create=mock_date.datetime.now(),
                                              user=mock_current_user)
        mock_find_next_display_priority_for_user.assert_called_once_with()
        mock_TodoList().save.assert_called_once()
        self.assertStatus(response, 302)
        self.assertRedirects(response, url_for('read_todo', priority=1, user=mock_current_user))

    @patch('flask_todo.flask_todo.current_user')
    def test_delete(self, mock_current_user):
        app.config['LOGIN_DISABLED'] = True
        response = self.client.post('/delete/1')
        datatest = TodoList.query.all()
        self.assertStatus(response, 302)
        self.assertRedirects(response, url_for('read_todo', user=mock_current_user))
        self.assertEqual(len(datatest), 1)

    @patch('flask_todo.flask_todo.current_user')
    def test_update_if(self, mock_current_user):
        string = {'priority': 1, 'text': 'text1', 'priority_old': 1}
        response = self.client.get('/update/1', query_string=string)
        self.assert200(response)
        self.assertTemplateUsed('update.html')
        self.assertContext('text', string['text'])
        self.assertContext('priority', str(1))
        self.assertContext('priority_old', str(1))
        self.assertContext('user', mock_current_user)

    @patch('flask_todo.flask_todo.current_user')
    def test_update_else(self, mock_current_user):
        data = {'priority': 3, 'text': 'update'}
        string = {'priority': 1}
        response = self.client.post('/update/1', data=data, query_string=string)
        datatest = TodoList.query.filter_by(id=1).first()
        self.assertStatus(response, 302)
        self.assertRedirects(response, url_for('read_todo', priority=1, user=mock_current_user))
        self.assertEqual(datatest.text, 'update')
        self.assertEqual(datatest.priority, 3)

    @patch('flask_todo.flask_todo.current_user')
    @patch('flask_todo.flask_todo.get_link')
    @patch('flask_todo.flask_todo.get_up_link')
    def test_up_exept(self, mock_get_up_link, mock_get_link, mock_current_user):
        mock1 = MagicMock()
        mock_get_link.return_value = mock1
        mock_get_up_link.side_effect = NoLink
        response = self.client.post('/up/10', query_string={'priority': 1})
        self.assertRedirects(response, url_for('read_todo', code=400, priority=1, user=mock_current_user))
        mock_get_link.assert_called_once_with('10')
        mock_get_up_link.assert_called_once_with(mock1, '1', mock_current_user)

    @patch('flask_todo.flask_todo.current_user')
    @patch('flask_todo.flask_todo.get_link')
    @patch('flask_todo.flask_todo.get_up_link')
    def test_up_try(self, mock_get_up_link, mock_get_link, mock_current_user):
        mock1 = MagicMock(display_priority=1)
        mock2 = MagicMock(display_priority=2)
        mock_get_link.return_value = mock1
        mock_get_up_link.return_value = mock2
        response = self.client.post('/up/10', query_string={'priority': 1})
        self.assertRedirects(response, url_for('read_todo', priority=1, user=mock_current_user))
        mock_get_link.assert_called_once_with('10')
        mock_get_up_link.assert_called_once_with(mock1, '1', mock_current_user)
        mock_get_link().save.assert_called_once()
        mock_get_up_link().save.assert_called_once()
        self.assertEqual(mock1.display_priority, 2)
        self.assertEqual(mock2.display_priority, 1)

    @patch('flask_todo.flask_todo.current_user')
    @patch('flask_todo.flask_todo.get_link')
    @patch('flask_todo.flask_todo.get_down_link')
    def test_down_exept(self, mock_get_down_link, mock_get_link, mock_current_user):
        mock1 = MagicMock()
        mock_get_link.return_value = mock1
        mock_get_down_link.side_effect = NoLink
        response = self.client.post('/down/10', query_string={'priority': 1})
        self.assertRedirects(response, url_for('read_todo', code=400, priority=1, user=mock_current_user))
        mock_get_link.assert_called_once_with('10')
        mock_get_down_link.assert_called_once_with(mock1, '1', mock_current_user)

    @patch('flask_todo.flask_todo.current_user')
    @patch('flask_todo.flask_todo.get_link')
    @patch('flask_todo.flask_todo.get_down_link')
    def test_down_try(self, mock_get_down_link, mock_get_link, mock_current_user):
        mock1 = MagicMock(display_priority=1)
        mock2 = MagicMock(display_priority=2)
        mock_get_link.return_value = mock1
        mock_get_down_link.return_value = mock2
        response = self.client.post('/down/10', query_string={'priority': 1})
        self.assertRedirects(response, url_for('read_todo', priority=1, user=mock_current_user))
        mock_get_link.assert_called_once_with('10')
        mock_get_down_link.assert_called_once_with(mock1, '1', mock_current_user)
        mock_get_link().save.assert_called_once()
        mock_get_down_link().save.assert_called_once()
        self.assertEqual(mock1.display_priority, 2)
        self.assertEqual(mock2.display_priority, 1)

    @patch('flask_todo.flask_todo.current_user')
    def test_done(self, mock_current_user):
        response = self.client.post('/done/1', query_string={'priority': 1})
        self.assertRedirects(response, url_for('read_todo', priority=1, user=mock_current_user))
        datatest = TodoList.query.filter_by(id=1).first()
        self.assertEqual(datatest.done, True)

    @patch('flask_todo.flask_todo.LoginForm')
    @patch('flask_todo.flask_todo.current_user')
    def test_login(self, mock_current_user, mock_login):
        response = self.client.get('/login')
        self.assert200(response)
        self.assertTemplateUsed('login.html')
        mock_login.assert_called_once()
        self.assertEqual(self.get_context_variable('user'), mock_current_user)
        self.assertEqual(self.get_context_variable('form'), mock_login())

    @patch('flask_todo.flask_todo.LoginForm')
    @patch('flask_todo.flask_todo.current_user')
    def test_login_post(self, mock_current_user, mock_login):
        mock1 = MagicMock()
        mock_login.return_value = mock1
        mock1.validate_on_submit.return_value = False
        # mock_login().validate_on_submit.return_value = False
        response = self.client.post('/login')
        self.assert400(response)
        self.assertTemplateUsed('login.html')
        mock_login.assert_called_once()
        self.assertEqual(self.get_context_variable('user'), mock_current_user)
        self.assertEqual(self.get_context_variable('form'), mock_login())

    @patch('flask_todo.flask_todo.flash')
    @patch('flask_todo.flask_todo.get_user_by_email_and_check_psw')
    @patch('flask_todo.flask_todo.LoginForm')
    @patch('flask_todo.flask_todo.current_user')
    def test_login_post_true_exept(self, mock_current_user, mock_login, mock_get_user, mock_flash):
        mock1 = MagicMock(email=MagicMock(data='mail'), psw=MagicMock(data='psw'))
        mock_login.return_value = mock1
        mock1.validate_on_submit.return_value = True
        mock_get_user.side_effect = NoUserOrPSW
        response = self.client.post('/login')
        mock_flash.assert_called_once_with('error with email or psw', category='error')
        self.assert400(response)
        self.assertTemplateUsed('login.html')
        mock_login.assert_called_once()
        self.assertEqual(self.get_context_variable('user'), mock_current_user)
        self.assertEqual(self.get_context_variable('form'), mock_login())

    @patch('flask_todo.flask_todo.login_user')
    @patch('flask_todo.flask_todo.get_user_by_email_and_check_psw')
    @patch('flask_todo.flask_todo.LoginForm')
    @patch('flask_todo.flask_todo.current_user')
    def test_login_post_true_try(self, mock_current_user,
                                 mock_login, mock_get_user, mock_login_user):
        mock1 = MagicMock(email=MagicMock(data='mail'),
                          psw=MagicMock(data='psw'),
                          remember=MagicMock(data=True))
        mock_login.return_value = mock1
        mock1.validate_on_submit.return_value = True
        mock2 = MagicMock()
        mock_get_user.return_value = mock2
        response = self.client.post('/login')
        self.assertStatus(response, 302)
        self.assertRedirects(response, url_for('read_todo', user=mock_current_user))
        mock_login.assert_called_once()
        mock_login_user.assert_called_once_with(mock2, remember=mock1.remember.data)

    @patch('flask_todo.flask_todo.RegisterForm')
    @patch('flask_todo.flask_todo.current_user')
    def test_register(self, mock_current_user, mock_register_form):
        response = self.client.get('/register')
        self.assert200(response)
        self.assertTemplateUsed('register.html')
        mock_register_form.assert_called_once()
        self.assertEqual(self.get_context_variable('user'), mock_current_user)
        self.assertEqual(self.get_context_variable('form'), mock_register_form())

    @patch('flask_todo.flask_todo.RegisterForm')
    @patch('flask_todo.flask_todo.current_user')
    def test_register_post_false(self, mock_current_user, mock_register_form):
        mock1 = MagicMock()
        mock_register_form.return_value = mock1
        mock1.validate_on_submit.return_value = False
        # mock_login().validate_on_submit.return_value = False
        response = self.client.post('/register')
        self.assert400(response)
        self.assertTemplateUsed('register.html')
        mock_register_form.assert_called_once()
        self.assertEqual(self.get_context_variable('user'), mock_current_user)
        self.assertEqual(self.get_context_variable('form'), mock_register_form())

    @patch('flask_todo.flask_todo.flash')
    @patch('flask_todo.flask_todo.check_user_name_and_email')
    @patch('flask_todo.flask_todo.RegisterForm')
    @patch('flask_todo.flask_todo.current_user')
    def test_register_post_true_if_false(self, mock_current_user,
                                         mock_register_form,
                                         mock_check_user,
                                         mock_flash):
        mock1 = MagicMock(email=MagicMock(data='mail'), psw=MagicMock(data='psw'))
        mock_register_form.return_value = mock1
        mock1.validate_on_submit.return_value = True
        mock_check_user.return_value = True
        response = self.client.post('/register')
        mock_flash.assert_called_once_with('user with email or name is used', category='error')
        self.assert400(response)
        self.assertTemplateUsed('register.html')
        mock_register_form.assert_called_once()
        self.assertEqual(self.get_context_variable('user'), mock_current_user)
        self.assertEqual(self.get_context_variable('form'), mock_register_form())

    @patch('flask_todo.flask_todo.User')
    @patch('flask_todo.flask_todo.generate_password_hash')
    @patch('flask_todo.flask_todo.flash')
    @patch('flask_todo.flask_todo.check_user_name_and_email')
    @patch('flask_todo.flask_todo.RegisterForm')
    @patch('flask_todo.flask_todo.current_user')
    def test_register_post_true_if_true(self, mock_current_user,
                                        mock_register_form,
                                        mock_check_user,
                                        mock_flash,
                                        mock_generate_psw,
                                        mock_create_user):
        mock1 = MagicMock(username=MagicMock(data='username'), email=MagicMock(data='mail'), psw=MagicMock(data='psw'))
        mock_register_form.return_value = mock1
        mock1.validate_on_submit.return_value = True
        mock_check_user.return_value = False
        mock2 = MagicMock()
        mock_create_user.return_value = mock2
        mock3 = MagicMock()
        mock_generate_psw.return_value = mock3
        response = self.client.post('/register')
        mock_flash.assert_called_once_with(f'user {mock1.username.data} was created', category='success')
        self.assertRedirects(response, url_for('login', user=mock_current_user))
        mock_create_user.assert_called_once_with(name=mock1.username.data, email=mock1.email.data, hash_password=mock3)
        mock_create_user().save.assert_called_once()
        mock_register_form.assert_called_once()
        mock_generate_psw.assert_called_once()
        mock_check_user.assert_called_once_with(mock1.username.data, mock1.email.data)
