import pytest

def add_something(x, y):
    return x + y


def my_decorator(function):
    def wrapper():
        new_value = 2 * 68
        print(new_value)
        function()
    return wrapper


class TestExample:
    def test_add_something(self):
        assert type(add_something(10, 1)) is int

    def test_add_something_1(self, preparing_for_test, second_preparing):
        print(second_preparing)
        for p in preparing_for_test:
            assert type(add_something(p, 2)) is not str


class TestExample1:

    @pytest.mark.smoke
    def test_add_something_2(self, preparing_for_test):
        for p in preparing_for_test:
            assert type(add_something(p, 1)) is int

    def test_add_something_4(self, preparing_for_test):
        for p in preparing_for_test:
            assert type(add_something(p, 2)) is not str
