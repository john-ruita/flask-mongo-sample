from marshmallow import Schema, fields, EXCLUDE, ValidationError, validates_schema


class StepSchema(Schema):
    """
    Schema for a step in solving a question.

    Attributes:
        Title (str): The title of the step.
        Result (str): The result or outcome of the step.
        ImageUrl (str, optional): The URL of an image related to the step.
    """
    class Meta:
        unknown = EXCLUDE

    Title = fields.Str(required=True)
    Result = fields.Str(required=True)
    ImageUrl = fields.Str(allow_none=True)


class StoreQuestionSchema(Schema):
    """
    Schema for storing a question.

    Attributes:
        Question (str): The question text.
        Options (list): A list of possible answers.
        CorrectAnswer (any): The correct answer, which can be of any type.
        Solution (str): The solution or explanation for the question.
        ImageUrl (str, optional): The URL of an image related to the question.
        Steps (list): A list of steps to solve the question, each step being a dictionary.
    """
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
        """
        Validate that the CorrectAnswer is in the Options list.

        Args:
            data (dict): The data to validate.
            **kwargs: Additional keyword arguments.

        Raises:
            ValidationError: If the CorrectAnswer is not in the Options list.
        """
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
