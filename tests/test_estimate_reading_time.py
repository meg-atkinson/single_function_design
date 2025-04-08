#import func and pytest
import pytest
from lib.estimate_reading_time import *

"""
Given a text of 200 words
It returns 1.0
"""
def test_estimate_with_200_words():
    text = " ".join(["word"] * 200)
    assert estimate_reading_time(text) == 1.0

"""
Given a text of 400 words
It returns 2.0
"""
def test_estimate_with_400_words():
    text = " ".join(["word"] * 400)
    assert estimate_reading_time(text) == 2.0

"""
Given a text of 300 words
It returns 1.5
"""
def test_estimate_with_300_words():
    text = " ".join(["word"] * 300)
    assert estimate_reading_time(text) == 1.5

"""
Given a text of 287 words
It returns 1.43 (rounded to two  decimal places)

"""
def test_estimate_with_287_words():
    text = " ".join(["word"] * 287)
    assert estimate_reading_time(text) == 1.44

"""
Given an empty string
It raises an error 
"""
def test_error_with_empty_string():
    text = ""
    with pytest.raises(Exception) as e:
        estimate_reading_time(text)
    error_message = str(e.value)
    assert error_message == "Empty text provided"
