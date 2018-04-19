from marshmallow import Schema, fields

from api.config import DATETIME_FORMAT


class PostSchema(Schema):
    event = fields.Str(required=True)
    timestamp = fields.DateTime(required=True, format=DATETIME_FORMAT)

    class Meta:
        strict = True
