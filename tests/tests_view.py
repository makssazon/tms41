from unittest.mock import patch

from flask_testing import TestCase
from flask_todo.flask_todo import app


class TestViews(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        return app

    @patch('flask_todo.flask_todo.get_todo_for_user')
    @patch('flask_todo.flask_todo.current_user')
    def test_profile_get_for_user(self, mock_current_user,
                                  mock_get_todo_for_user):
        app.config['LOGIN_DISABLED'] = True
        mock_get_todo_for_user.return_value = []
        response = self.client.get('/')
        self.assert200(response)
        self.assertEqual(self.get_context_variable('user'), mock_current_user)
