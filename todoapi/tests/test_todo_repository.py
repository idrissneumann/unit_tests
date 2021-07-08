import json

from db_connection import DbConnection
from todo_repository import TodoRepository
from todo_model import TodoModelGenerator
from todo_schema import TodoSchemaGenerator

from unittest import TestCase
from unittest.mock import patch

class Query():
    def all(self):
        return None

class Schema():
    def dump(self, obj):
        return json.dump(obj)

class TestRepository(TestCase):
    @patch('flask_sqlalchemy.SQLAlchemy', autospec = True)
    @patch.object(DbConnection, '__init__', lambda x, y: None)
    def test_create_all(self, db_mock):
        with patch.object(DbConnection, 'get_db', lambda x: db_mock):
            # Given
            app = None
            repository = TodoRepository(app)

            # When
            repository.create_all()

            # Then
            self.assertTrue(db_mock.create_all.called) # test that the sqlalchemy has been invoked
            self.assertEqual(1, db_mock.create_all.call_count) # test exactly once invocation

    @patch('flask_sqlalchemy.SQLAlchemy', autospec = True)
    @patch('tests.test_todo_repository.Query', autospec = True)
    @patch('tests.test_todo_repository.Schema', autospec = True)
    @patch.object(DbConnection, '__init__', lambda x, y: None)
    @patch.object(TodoModelGenerator, 'get_model', lambda x: None)
    @patch.object(Schema, 'dump', lambda x, y: json.dumps(y))
    @patch.object(Query, 'all', lambda: {"todos": [{"id": 1, "title": "test", "todo_description": "desc"}]})
    def test_get_all(self, schema_mock, query_mock, db_mock):
        with patch.object(DbConnection, 'get_db', lambda x: db_mock):
            with patch.object(TodoModelGenerator, 'query', lambda x: query_mock):
                with patch.object(TodoSchemaGenerator, 'get_schema', lambda x, many: schema_mock):
                    # Given
                    app = None
                    repository = TodoRepository(app)

                    # When
                    repository.get_all()

                    # Then
                    self.assertTrue(query_mock.all.called)
                    self.assertTrue(schema_mock.dump.called)
