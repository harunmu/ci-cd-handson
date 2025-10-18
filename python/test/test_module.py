from src.module import isEven
import pytest

def test_isEven():
    assert isEven(2) == True
    assert isEven(3) == False
    assert isEven(0) == True
    assert isEven(-2) == True
    assert isEven(-3) == False

def test_isEven_with_non_integer():
    with pytest.raises(TypeError):
        isEven("string")