from flask import Blueprint, request, jsonify
from flask_restx import Api, Namespace
from api.validation.TaskInschema import TaskInSchema
from config.db import SessionLocal
from repositories.TaskRepository import SqlAlchemyTaskRepository
from services.task_service import TaskService

task_bp = Blueprint("tasks", __name__, url_prefix="/tasks")
task_api = Api(task_bp)
task_ns = Namespace("task_ns", description="tasks")
task_api.add_namespace(task_ns)


@task_bp.route('', methods=['POST'])
def create_task():
    payload = request.get_json()
    data = TaskInSchema.parse_obj(payload)
    with SessionLocal() as session:
        task_repo = SqlAlchemyTaskRepository(session)
        task_service = TaskService(task_repo)
        task = task_service.create_task(title=data.title, description=data.description, status=data.status)
        return task, 201


@task_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    with SessionLocal() as session:
        task_repo = SqlAlchemyTaskRepository(session)
        task_service = TaskService(task_repo)
        task = task_service.get_task(task_id)
        return jsonify({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "created_at": task.created_at,
            "updated_at": task.updated_at

        }

        )


# Flask’s jsonify internally uses Python’s json.dumps().
#
# By default, Flask configures json.dumps() with sort_keys=True.
#
# That’s why the output is alphabetically ordered, even if you defined them in a different sequence.


@task_bp.route('<int:task_id>', methods=["PUT", "PATH"])
def update_task(task_id):
    payload = request.get_json()
    with SessionLocal() as session:
        task_repo = SqlAlchemyTaskRepository(session)
        task_service = TaskService(task_repo)
        task_service.update_task(task_id, **payload)


#
# Great question 👍
#
# Let’s break it down:
#
# payload = request.get_json()
# task = service.update_task(task_id, **payload)
#
# 1. request.get_json()
#
# In Flask, this reads the JSON body of the request and returns a Python dict.
#
# Example request body:
#
# {
#     "title": "demo1",
#     "description": "just for demo purpose",
#     "status": "completed"
# }
#
#
# After request.get_json(), you get:
#
# payload = {
#     "title": "demo1",
#     "description": "just for demo purpose",
#     "status": "completed"
# }
#
# 2. **payload
#
# ** is dictionary unpacking in Python.
#
# It takes the keys/values from the dictionary and passes them as keyword arguments to the function.
#
# So:
#
# service.update_task(task_id, **payload)
#
#
# is equivalent to:
#
# service.update_task(
#     task_id,
#     title="demo1",
#     description="just for demo purpose",
#     status="completed"
# )
#
# 3. Why use **payload?
#
# It makes the function call flexible.
#
# Instead of manually pulling out each key, you just unpack the dict.
#
# Your service method can define parameters like this:
#
# def update_task(self, task_id: int, title: str, description: str, status: str):
#     ...
#
#
# and Flask will automatically feed the values from payload.
#
# ⚠️ One thing to be careful about:
# If your JSON contains extra fields that update_task does not expect, Python will raise a TypeError.
#
# 👉 That’s why in production code, developers often validate payload with something like Pydantic before doing **payload.


@task_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    with SessionLocal() as session:
        task_repo = SqlAlchemyTaskRepository(session)
        task_service = TaskService(task_repo)
        task_service.delete_task(task_id)
