import pytest

"""
This file helps test the fixture code written in confest.py by running 
`pytest -k divisible -v` in the terminal.
"""

def test_divisible_by_13(input_value):
   assert input_value % 13 == 0