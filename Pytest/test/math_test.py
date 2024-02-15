import pytest
import Source.math as math

def test_add():
    result =math.add(number_one = 2, number_two= 5) 
    assert result == 7