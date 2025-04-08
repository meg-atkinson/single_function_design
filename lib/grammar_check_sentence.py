#File: grammar_check_sentence.py
def grammer_check_sentence(text):
    correct_marks = [".", "!", "?"]
    if text == "":
        raise Exception("Empty text provided")
    if text[0].isupper() and (any(text[-1] in mark for mark in correct_marks)):
        return True
    return False 