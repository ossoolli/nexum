import json

def evaluate_necessity(error_type):
    if error_type in ['json_error', 'syntax_error']:
        return False
    return True
