DOCUMENT_MODEL = {
    'source': "",
    'difficulty': "",
    'company': "",
    'answer_format': "",
    'topic': "",
    'score': 0,
    'question': {
        'number': 0,
        'data': ""
    },
    'attempts': [
        # contains ATTEMPT_MODEL instances
    ]
}

ATTEMPT_MODEL = {g
    'date': "",
    'code': "",
    'grading': {
        'requirements': 0,
        'algo_design': 0,
        'implementation': 0,
        'testing': 0
    },
    'notes': ""
}