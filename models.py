from db import db

class TaskModel(db.Model):
    __tablename__ = "Tasks"
    id = db.Column(db.Integer, primary_key = True)
    desc = db.Column(db.String(128))
    status = db.Column(db.String(64))

    def __init__(self,desc):
        self.desc = desc
        self.status = "In Progress"


class FinishedTaskModel(db.Model):
    __tablename__ = "FinishedTasks"
    id = db.Column(db.Integer, primary_key = True)
    desc = db.Column(db.String(128))
    status = db.Column(db.String(64))

    def __init__(self,desc):
        self.desc = desc
        self.status = "Completed"
