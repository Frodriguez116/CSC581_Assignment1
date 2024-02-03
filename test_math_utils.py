
import pytest
from math_utils import MathUtils

@pytest.fixture
def math_utils_instance():
    return MathUtils()

def test_add():
    assert MathUtils.add(2, 3) == 5
    assert MathUtils.add(-2, 3) == 1
    assert MathUtils.add(0, 0) == 0

def test_subtract():
    assert MathUtils.subtract(5, 3) == 2
    assert MathUtils.subtract(-2, -3) == 1
    assert MathUtils.subtract(0, 0) == 0

def test_multiply():
    assert MathUtils.multiply(2, 3) == 6
    assert MathUtils.multiply(-2, 3) == -6
    assert MathUtils.multiply(0, 5) == 0

def test_divide():
    assert MathUtils.divide(6, 3) == 2
    assert MathUtils.divide(-6, 3) == -2
    assert MathUtils.divide(0, 5) == 0

def test_divide_by_zero():
    assert MathUtils.divide(5, 0) == -1.0
    assert MathUtils.divide(-10, 0) == -1.0
    assert MathUtils.divide(0, 0) == -1.0

# Additional test using fixture
def test_add_with_fixture(math_utils_instance):
    assert math_utils_instance.add(2, 3) == 5
    assert math_utils_instance.add(-2, 3) == 1
    assert math_utils_instance.add(0, 0) == 0
