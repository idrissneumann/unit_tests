from flask import Flask, request, jsonify, make_response

import os

from todo_schema import TodoSchemaGenerator
from todo_model import TodoModelGenerator
from db_connection import DbConnection

app = Flask(__name__)

host = os.environ['TODO_HOST']
port = os.environ['TODO_PORT']

connection = DbConnection(app)
db = connection.get_db()
model_generator = TodoModelGenerator(db)
model = model_generator.get_model()

schema = TodoSchemaGenerator(db, model)

db.create_all()

@app.route('/api/v1/todo', methods=['GET'])
def index():
    get_todos = model.query.all()
    todo_schema = schema.get_schema(many=True)
    todos = todo_schema.dump(get_todos)
    return make_response(jsonify({"todos": todos}))

@app.route('/api/v1/todo/<id>', methods=['GET'])
def get_todo_by_id(id):
    get_todo = model.query.get(id)
    todo_schema = schema.get_schema()
    todo = todo_schema.dump(get_todo)
    return make_response(jsonify({"todo": todo}))

@app.route('/api/v1/todo/<id>', methods=['PUT'])
def update_todo_by_id(id):
    data = request.get_json()
    get_todo = model.query.get(id)
    if data.get('title'):
        get_todo.title = data['title']
    if data.get('todo_description'):
        get_todo.todo_description = data['todo_description']
    db.session.add(get_todo)
    db.session.commit()
    todo_schema = schema.get_schema(only=['id', 'title', 'todo_description'])
    todo = todo_schema.dump(get_todo)
    return make_response(jsonify({"todo": todo}))

@app.route('/api/v1/todo/<id>', methods=['DELETE'])
def delete_todo_by_id(id):
    get_todo = model.query.get(id)
    db.session.delete(get_todo)
    db.session.commit()
    return make_response("", 204)

@app.route('/api/v1/todo', methods=['POST'])
def create_todo():
    data = request.get_json()
    todo_schema = schema.get_schema()
    todo = todo_schema.load(data)
    result = todo_schema.dump(todo.create())
    return make_response(jsonify({"todo": result}), 200)

if __name__ == "__main__":
    app.run(debug=False, host=host, port=port)
