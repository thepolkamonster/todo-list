from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class NewTask(FlaskForm):
    task = StringField(validators=[DataRequired()])
    create = SubmitField("Create")

class Task(FlaskForm):
    task_id = IntegerField()
    delete = SubmitField("Delete")
    completed = SubmitField("Completed")

class TaskDel(FlaskForm):
    task_id = IntegerField()
    delete = SubmitField("Delete")
    undo = SubmitField("Undo")