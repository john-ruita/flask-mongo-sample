from marshmallow import Schema, fields, EXCLUDE, ValidationError, validates_schema


class StepSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    Title = fields.Str(required=True)
    Result = fields.Str(required=True)
    ImageUrl = fields.Str(allow_none=True)

class StoreQuestionSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    Question = fields.Str(required=True)
    Options = fields.List(fields.Str(), required=True)
    CorrectAnswer = fields.Raw(required=True)
    Solution = fields.Str(required=True)
    ImageUrl = fields.Str(allow_none=True)
    Steps = fields.List(fields.Nested(StepSchema), required=True)

    @validates_schema
    def validate_correct_answer(self, data, **kwargs):
        options = data.get("Options", [])
        correct_answer = data.get("CorrectAnswer")

        if isinstance(correct_answer, int):
            if not (0 <= correct_answer < len(options)):
                raise ValidationError(
                    "CorrectAnswer must be in the Options list.",
                    field_name="CorrectAnswer"
                )
        elif correct_answer not in options:
            raise ValidationError(
                "CorrectAnswer must be in the Options list.",
                field_name="CorrectAnswer"
            )
