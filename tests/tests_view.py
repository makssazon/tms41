from unittest.mock import patch, MagicMock

from flask import url_for
from flask_testing import TestCase
from flask_todo.flask_todo import app


class TestViews(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        return app

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
