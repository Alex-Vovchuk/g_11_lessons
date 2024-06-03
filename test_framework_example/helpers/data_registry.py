import random
import string


class DataRegistry:
    _registry = {}

    @classmethod
    def add_first_name(cls, first_name, mask):
        unique_first_name = cls.generate_first_name(first_name, mask)
        cls._registry[unique_first_name] = first_name

    @classmethod
    def generate_first_name(cls, first_name, mask):
        random_letters = ''.join(random.choice(string.digits))
        return first_name + random_letters + mask

    @classmethod
    def is_first_name_unique(cls, first_name):
        return first_name not in cls._registry
