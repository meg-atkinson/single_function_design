#import libraries and function
import pytest
from lib.grammar_check_sentence import *

#test if text starts with cap and ends with full stop returns True
def test_starts_with_cap_ends_with_full_stop():
    result = grammer_check_sentence("Hello darkness my old friend.")
    assert result == True

#test if text starts with cap and ends with question mk returns True
def test_starts_with_cap_ends_with_q_mark():
    result = grammer_check_sentence("Hello darkness my old friend?") 
    assert result == True

#test if text starts with cap and ends with excl amk returns True
def test_starts_with_cap_ends_with_excl_mark():
    result = grammer_check_sentence("Hello darkness my old friend!")
    assert result == True

#testif upper case start and no punct at end returns False
def test_starts_with_upper_case_ends_with_no_punct():
    result = grammer_check_sentence("Hello darkness my old friend") 
    assert result == False


#test if lower case start and no punct at end returns False
def test_starts_with_lower_case_ends_with_no_punct():
    result = grammer_check_sentence("hello darkness my old friend") 
    assert result == False

#test if start with lower case but end with correct punctuation returns False
def test_starts_with_lower_case_ends_with_full_stop():
    result = grammer_check_sentence("hello darkness my old friend.")
    assert result == False

#test if start with lower case and end with incorrect punctuation returns False
def test_starts_with_lower_case_ends_with_comma():
    result = grammer_check_sentence("hello darkness my old friend,") 
    assert result == False

#test if give empty string it raises an error
def test_empty_string_raises_error():
    with pytest.raises(Exception) as e:
        grammer_check_sentence("") 
    error_message = str(e.value)
    assert error_message == "Empty text provided"



