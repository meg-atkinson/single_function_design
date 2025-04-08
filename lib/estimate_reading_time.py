# File: estimate_reading_time.py
def estimate_reading_time(text):
    if text == "":
        raise Exception("Empty text provided")
    words = text.split()
    return round(len(words) / 200, 2)