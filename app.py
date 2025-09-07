from flask import Flask
from sqlalchemy import inspect
from entities import task
from api.endpoints.flask_api import task_bp
from config.db import Base, engine

Base.metadata.create_all(bind=engine)

# Debug: show tables in DB
inspector = inspect(engine)
print("Tables in DB:", inspector.get_table_names())


def create_app():
    app = Flask(__name__)
    app.register_blueprint(task_bp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, use_reloader=False)
