import random
import string
import secrets

class LogPass:

    # Генерируем почту
    def generate_mail(self, length):
        name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        domain = ['@mail.ru', '@gmail.com', '@yandex.ru']
        mail = f'{name}{random.choice(domain)}'
        return mail

    # Генерируем пароль
    def generate_secure_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password