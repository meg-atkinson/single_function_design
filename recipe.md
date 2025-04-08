# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

> As a user
> So that I can manage my time
> I want to see an estimate of reading time for a text, assuming that I > can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def estimate_reading_time(text):
    """Estimates reading time for a given text on basis can read 200 words per minute

    Parameters: (list all parameters and their types)
        text: string representing human readable text

    Returns: (state the return value and its type)
        a float, representing reading time in minutes

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
Given a text of 200 words
It returns 1.0
"""
estimate_reading_time("...200...") 
#=> 1.0

"""
Given a text of 400 words
It returns 2.0
"""
estimate_reading_time("...400...") 
#=> 2.0

"""
Given a text of 300 words
It returns 1.5

"""
estimate_reading_time("...300...") 
#=> 1.5

"""
Given a text of 287 words
It returns 1.44 (1.435 rounded to two  decimal places)

"""
estimate_reading_time("...287...") 
#=> 1.44

"""
Given an empty string
It raises an error 
"""
estimate_reading_time("") 
# raises error: "Empty text provided"

"""

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


