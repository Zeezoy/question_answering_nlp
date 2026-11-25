
QUESTION_TYPE = ("PERSON", "DATE", "LOCATION", "NUMBER", "DESCRIPTION")


def get_answer_type(question_type: str) -> str:
    table = {
        "WHO": "PERSON",
        "WHEN": "DATE",
        "WHERE": "LOCATION",
        "HOW_MANY": "NUMBER",
        "WHAT": "DESCRIPTION" 
    }

    return table.get(question_type, "DESCRIPTION")