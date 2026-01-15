
import math
import pytest
from calcpkg import calculate

@pytest.mark.parametrize("expr, expected", [
    ("1+1", 2.0),
    ("1 + 2 * 3", 7.0),
    ("(1 + 2) * 3", 9.0),
    ("-5 + 2", -3.0),
    ("1 + 2 * (3 - 1) / 4", 2.0),
    ("3/2", 1.5),
    ("+3", 3.0),
])
def test_calculate_ok(expr, expected):
    assert math.isclose(calculate(expr), expected, rel_tol=1e-9, abs_tol=1e-12)

@pytest.mark.parametrize("expr", [
    "", " ", "abc", "__import__(\"os\")", "1//2", "2**3", "max(1,2)",
])
def test_calculate_invalid(expr):
    with pytest.raises(ValueError):
        calculate(expr)

def test_div_by_zero():
    with pytest.raises(ValueError):
        calculate("1/0")
