from flask import render_template, redirect, url_for
from flask_smorest import Blueprint
from forms import NewTask, Task, TaskDel
from models import TaskModel, FinishedTaskModel
from db import db

blp = Blueprint("views", __name__, description = "The front end views")

@blp.route('/', methods = ["GET","POST"])
def index():
    newtask = NewTask()
    taskform = Task()

    if newtask.validate_on_submit():
        t_desc= newtask.task.data
        temp_task = TaskModel(t_desc)
        db.session.add(temp_task)
        db.session.commit()
        return redirect(url_for('views.index'))
    
    if taskform.validate_on_submit():
        if taskform.delete.data == True:
            id_req = taskform.task_id.data
            task = TaskModel.query.get(id_req)
            db.session.delete(task)
            db.session.commit()
        elif taskform.completed.data == True:
            id_req = taskform.task_id.data
            task = TaskModel.query.get(id_req)
            comp_task = FinishedTaskModel(task.desc)
            db.session.delete(task)
            db.session.add(comp_task)
            db.session.commit()
            

        return redirect(url_for('views.index'))
    all_tasks = TaskModel.query.all()
    return render_template('index.html', newtask = newtask, all_tasks = all_tasks, taskform = taskform)

@blp.route('/finished', methods = ["GET","POST"])
def finished():
    taskdel = TaskDel()
    if taskdel.validate_on_submit():
        if taskdel.delete.data == True:
            id_req = taskdel.task_id.data
            task = FinishedTaskModel.query.get(id_req)
            db.session.delete(task)
            db.session.commit()
        elif taskdel.undo.data == True:
            id_req = taskdel.task_id.data
            task = FinishedTaskModel.query.get(id_req)
            pend_task = TaskModel(task.desc)
            db.session.delete(task)
            db.session.add(pend_task)
            db.session.commit()
        return redirect(url_for('views.finished'))
    
    all_tasks = FinishedTaskModel.query.all()

    return render_template('finished.html', taskdel = taskdel, all_tasks = all_tasks)