from marshmallow import Schema, fields

class TaskSchema(Schema):
    id = fields.Integer(dump_only = True)
    desc = fields.String(required=True)
    status = fields.String()

class TaskInputSchema(Schema):
    desc = fields.String(required=True)