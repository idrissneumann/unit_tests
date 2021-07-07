from db_connection import DbConnection
from todo_repository import TodoRepository
from todo_model import TodoModelGenerator
from todo_schema import TodoSchemaGenerator

from unittest import TestCase
from unittest.mock import patch

class TestRepository(TestCase):
    @patch('flask_sqlalchemy.SQLAlchemy', autospec = True)
    def test_create_all(self, db_mock):
        # Given 
        with patch.object(DbConnection, 'get_db', lambda x: db_mock):
            with patch.object(TodoModelGenerator, 'get_model', lambda x: None):
                with patch.object(TodoSchemaGenerator, 'get_schema', lambda x, y, z: None):
                    with patch.object(DbConnection, '__init__', lambda x, y: None):
                        app = None
                        repository = TodoRepository(app)

        # When
        repository.create_all()

        # Then
        self.assertTrue(db_mock.create_all.called) # test that the sqlalchemy has been invoked
        self.assertEqual(1, db_mock.create_all.call_count) # test exactly once invocation
