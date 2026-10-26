from re import match
import pytest

from app.discount import calculate_discount


def test_calculate_discount():
    assert calculate_discount(100, 20) == 80


def test_full_discount():
    assert calculate_discount(100, 100) == 0


def test_zero_discount():
    assert calculate_discount(100, 0) == 100


def test_negative_price_raises_error():
    with pytest.raises(
        ValueError,
        match="Price cannot be negative.",
    ):
        calculate_discount(-100, 20)


def test_invalid_discount_raises_error():
    with pytest.raises(
        ValueError,
        match="Discount must be between 0 and 100.",
    ):
        calculate_discount(100, 120)
