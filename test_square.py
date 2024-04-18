import pytest
import math

"""
Pytest allows us to use markers on test functions. Markers are used to set various features/attributes to test functions. Pytest provides many inbuilt markers such as xfail, skip and parametrize. Apart from that, users can create their own marker names.

To use markers, we have to import pytest module in the test file. We can define our own marker names to the tests and run the tests having those marker names. Finally, register markers in pytest.ini file to run tests with markers.
"""

@pytest.mark.square
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

@pytest.mark.square
def testsquare():
   num = 7
   assert 7*7 == 40

@pytest.mark.others
def test_equality():
   assert 10 == 11