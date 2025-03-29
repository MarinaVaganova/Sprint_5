import random
import string


# Генерация логина и пароля
class TestGenerator:
    name = 'marina'
    surname = 'vaganova'
    cogort_number = '20'
    domain = 'yandex.ru'

    @staticmethod
    def generate_random_digits(length = 3):
        return ''.join(random.choices(string.digits, k = length))

    @classmethod
    def generate_email(cls):
        test_email = f'{cls.name}_{cls.surname}_{cls.cogort_number}_{cls.generate_random_digits()}@{cls.domain}'
        return test_email

    @staticmethod
    def generate_password(length = 6):
        test_password = ''.join(random.choices(string.ascii_letters + string.digits, k = length))
        return test_password