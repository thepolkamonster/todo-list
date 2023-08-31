from db import db
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from models import TaskModel, FinishedTaskModel
from sqlalchemy.exc import SQLAlchemyError
from schemas import TaskSchema

blp = Blueprint("routes", __name__, description = "The api routes Blueprint")

@blp.route("/api/tasks")
class TaskRoute(MethodView):
    @blp.response(200, TaskSchema(many = True))

    def get(self):
        res = TaskModel.query.all()
        return res