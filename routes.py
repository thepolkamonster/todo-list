from db import db
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from models import TaskModel, FinishedTaskModel
from sqlalchemy.exc import SQLAlchemyError
from schemas import TaskSchema, TaskInputSchema

blp = Blueprint("routes", __name__, description = "The api routes Blueprint")

@blp.route("/api/tasks")
class TaskRoute(MethodView):

    @blp.response(200, TaskSchema(many = True))
    def get(self):
        res = TaskModel.query.all()
        return res
    

    @blp.arguments(TaskInputSchema)
    @blp.response(200, TaskSchema)
    def post(self, TaskData):
        temp_task = TaskModel(**TaskData)
        try:
            db.session.add(temp_task)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message = "Error while inserting")
        return temp_task
    
@blp.route("/api/finishedtasks")
class FinishedTaskRoute(MethodView):

    @blp.response(200, TaskSchema(many = True))
    def get(self):
        res = FinishedTaskModel.query.all()
        return res
    
@blp.route("/api/tasks/<string:id_req>")
class TaskRouteId(MethodView):

    @blp.response(200, TaskSchema)
    def delete(self, id_req):
        res = TaskModel.query.get_or_404(id_req)
        db.session.delete(res)
        db.session.commit()

        return res
