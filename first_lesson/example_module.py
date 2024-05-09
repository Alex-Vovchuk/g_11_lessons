def validate_password(password):
    if len(password) < 8:
        return False

    if not any(char.isupper() for char in password):
        return False

    special_chars = "!@#$%^&*()-+=_"
    if not any(char in special_chars for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    return True
