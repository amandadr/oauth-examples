import pytest

"""
We can define fixture functions in this file to make them accessible across multiple test files.
"""

@pytest.fixture
def input_value():
   input = 39
   return input