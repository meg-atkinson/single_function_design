# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

> As a user
> So that I can improve my grammar
> I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def starts_with_capital_ends_with_suitable_mark(text):
    """verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

    Parameters: (list all parameters and their types)
        text: string representing human readable text

    Returns: (state the return value and its type)
        a boolean, representing whether text passes test

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text starting with capital but ending with no punct
It returns False
"""


"""
Given a text of 400 words
It returns 2.0
"""


"""
Given a text of 300 words
It returns 1.5

"""


"""
Given a text of 287 words
It returns 1.44 (1.435 rounded to two  decimal places)

"""


"""
Given an empty string
It raises an error 
"""


"""

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


