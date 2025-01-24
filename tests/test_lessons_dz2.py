import pytest
from lesson_DZ import bankOOP_dz2


def test_bankOOP():
    assert bankOOP_dz2.accaunt_igor.get_balance() > 0, "баланс меньше нуля"
