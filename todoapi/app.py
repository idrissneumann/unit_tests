from flask import Flask, request, jsonify, make_response
from todo_repository import TodoRepository

import os

global app 
global host
global port

app = None
host = None
port = None

def init_app():
    global app 
    global host
    global port

    if app is None:
        app = Flask(__name__)

    if host is None:
        host = os.environ['TODO_HOST']

    if port is None:
        port = os.environ['TODO_PORT']

init_app()
repository = TodoRepository(app)
repository.create_all()

@app.route('/api/v1/todo', methods=['GET'])
def index():
    return make_response(jsonify({"todos": repository.get_all()}))

@app.route('/api/v1/todo/<id>', methods=['GET'])
def get_todo_by_id(id):
    return make_response(jsonify({"todo": repository.get(id)}))

@app.route('/api/v1/todo/<id>', methods=['PUT'])
def update_todo_by_id(id):
    data = request.get_json()
    return make_response(jsonify({"todo": repository.update(id, data)}))

@app.route('/api/v1/todo/<id>', methods=['DELETE'])
def delete_todo_by_id(id):
    repository.delete(id)
    return make_response("", 204)

@app.route('/api/v1/todo', methods=['POST'])
def create_todo():
    data = request.get_json()
    return make_response(jsonify({"todo": repository.insert(data)}), 200)

if __name__ == "__main__":
    app.run(debug=False, host=host, port=port)
