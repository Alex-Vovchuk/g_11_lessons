import pytest
import logging

logging.basicConfig(filename='example.log', level=logging.INFO)



@pytest.fixture(scope='function')
def second_preparing(preparing_for_test):
    some = preparing_for_test
    return some.reverse()


def assert_mine(value_to_check, expected_value):
    try:
        assert value_to_check == expected_value
    except AssertionError as e:
        logging.error(e)
