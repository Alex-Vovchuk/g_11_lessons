import pytest
from first_lesson.example_module import validate_password


@pytest.mark.parametrize("wrong_password", ['Pa!s2w', 'Password1', "<PASSWddfD>"])
def test_validate_password(wrong_password):
    assert not validate_password(wrong_password)


def add_something(x, y):
    return x + y


@pytest.mark.parametrize("first_arg, second_arg, expected_result", [(1, 2, 3), (5, 8, 13), (5, 3, 16)])
def test_add_something(first_arg, second_arg, expected_result):
    assert add_something(first_arg, second_arg) == expected_result
