import pytest

from app.calculator import add, divide

# Fixture: provides reusable test data
@pytest.fixture
def addition_cases():
    return [
        (2, 3, 5),
        (-2, 2, 0),
        (0, 0, 0),
        (-3, -4, -7),
    ]


# Test 1: Basic addition
def test_add():
    assert add(2, 3) == 5


# Test 2: Parametrized addition tests
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-2, 2, 0),
        (0, 0, 0),
        (-3, -4, -7),
        (10, -5, 5),
    ],
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected


# Test 3: Use a fixture to test multiple addition cases
def test_add_with_fixture(addition_cases):
    for a, b, expected in addition_cases:
        assert add(a, b) == expected


# Test 4: Basic division
def test_divide():
    assert divide(10, 2) == 5


# Test 5: Division with a decimal result
def test_divide_decimal_result():
    assert divide(7, 2) == 3.5


# Test 6: Division of negative numbers
def test_divide_negative_numbers():
    assert divide(-10, 2) == -5


# Test 7: Division by zero raises ValueError
def test_divide_by_zero():
    with pytest.raises(
        ValueError,
        match="Cannot divide by zero.",
    ):
        divide(10, 0)
