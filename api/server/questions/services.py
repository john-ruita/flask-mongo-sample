import bson

from .validation import StoreQuestionSchema
from .. import mongo
from ..utils.helpers import generate_response, paginate
from ..utils.http_codes import HTTP_422_UNPROCESSABLE_ENTITY


def retrieve_question(slug, action="Retrieved"):
    """
    Retrieve a question from the database by its slug.

    Args:
        slug (str): The unique identifier of the question.
        action (str): The action performed, default is "Retrieved".

    Returns:
        Response: A Flask response object containing the question data and a message.
    """
    document = mongo.db.questions.find_one_or_404({"_id": bson.ObjectId(slug)})
    document["_id"] = str(document["_id"])
    return generate_response(data=document, message=f"Question {action}")

def post_question(body):
    """
    Insert a new question into the database.

    Args:
        body (dict): The data of the question to be inserted.

    Returns:
        Response: A Flask response object containing the inserted question data and a message.
    """
    validator = StoreQuestionSchema()
    errors = validator.validate(body)
    if errors:
        return generate_response(data=errors, message="Validation error", status=HTTP_422_UNPROCESSABLE_ENTITY)
    document = mongo.db.questions.insert_one(body)
    return retrieve_question(str(document.inserted_id), action="Created")

def update_question(slug, body):
    """
    Update an existing question in the database.

    Args:
        slug (str): The unique identifier of the question.
        body (dict): The updated data of the question.

    Returns:
        Response: A Flask response object containing the updated question data and a message.
    """
    validator = StoreQuestionSchema()
    errors = validator.validate(body)
    if errors:
        return generate_response(data=errors, message="Validation error", status=HTTP_422_UNPROCESSABLE_ENTITY)
    mongo.db.questions.update_one({"_id": bson.ObjectId(slug)}, {"$set": body})
    return retrieve_question(slug, action="Updated")

def delete_question(slug):
    """
    Delete a question from the database by its slug.

    Args:
        slug (str): The unique identifier of the question.

    Returns:
        Response: A Flask response object containing a message indicating the question was deleted.
    """
    mongo.db.questions.delete_one({"_id": bson.ObjectId(slug)})
    return generate_response(data={}, message="Question deleted")

@paginate
def list_questions(page, per_page):
    """
    List questions from the database with pagination.

    Args:
        page (int): The page number to retrieve.
        per_page (int): The number of questions per page.

    Returns:
        Response: A Flask response object containing the paginated questions data, a message, the current page, and the total number of questions.
    """
    documents = mongo.db.questions.find().skip((page - 1) * per_page).limit(per_page)
    data = [{**document, "_id": str(document["_id"])} for document in documents]
    total = mongo.db.questions.count_documents({})
    return generate_response(data=data, message="Questions retrieved", page=page, total=total)
