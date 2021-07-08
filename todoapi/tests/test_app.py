from flask import Flask

from unittest import TestCase
from unittest.mock import Mock, patch

from todo_repository import TodoRepository

class TestApp(TestCase):
    def get_app(self):
        global app
        global port
        global host

        app = Flask(__name__)
        app.config['TESTING'] = True
        port = 8080
        host = '127.0.0.1'
        return app

    @patch('todo_repository.TodoRepository.get_all', side_effect = lambda: [{"id": 1, "title": "test", "todo_description": "desc"}])
    @patch.object(TodoRepository, '__init__', lambda x, y: None)
    @patch.object(TodoRepository, 'create_all', lambda x: None)
    def test_index(self, method_mock):
        with self.get_app().app_context():
            # Given
            from app import index

            # When
            result = index()

            # Then
            self.assertIsNotNone(result)
            method_mock.assert_called_once()

    @patch('todo_repository.TodoRepository.get', side_effect = lambda id: {"id": 1, "title": "test", "todo_description": "desc"})
    @patch.object(TodoRepository, '__init__', lambda x, y: None)
    @patch.object(TodoRepository, 'create_all', lambda x: None)
    def test_get_todo_by_id(self, method_mock):
        with self.get_app().app_context():
            # Given
            from app import get_todo_by_id
            id = 1

            # When
            result = get_todo_by_id(id)

            # Then
            self.assertIsNotNone(result)
            method_mock.assert_called_once_with(id)

    def test_update_todo_by_id(self):
        # TODO implement the right test here
        self.assertTrue(True)

    def test_delete_todo_by_id(self):
        # TODO implement the right test here
        self.assertTrue(True)

    def test_create_todo(self):
        # TODO implement the right test here
        self.assertTrue(True)

