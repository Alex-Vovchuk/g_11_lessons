from first_lesson.example_module import validate_password


def test_second_validate_password():
    my_password = 'Password9!'
    assert validate_password(my_password)
