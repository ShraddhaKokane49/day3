import pytest
from calculator import add
from calculator import sub


def test_add():
	assert add(2, 3) == 5
	assert add(-1, 1) == 0
	assert add(2.5, 0.5) == 3.0


def test_sub():
	assert sub(5, 3) == 2
	assert sub(0, 5) == -5


