from marshmallow import Schema, fields


class PostSchema(Schema):
    event = fields.Str(required=True)
    # adicionar validacao para timestamp
    timestamp = fields.Str(required=True)

    class Meta:
        strict = True
