from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_model import Base_model
import random
import string
import secrets

class Registration_page(Base_model):

    user_name_input = '//fieldset[1]/div/div/input[@type="text"]'#Поле ввода имени
    user_mail_input = '//fieldset[2]/div/div/input[@type="text"]'#Поле ввода почты
    user_password_input = '//fieldset[3]/div/div/input[@type="password"]'#Поле ввода пароля
    error_msg = '//p[@class="input__error text_type_main-default"]' #Сообщение об ошибке пароля

    # получаем сообщение об ошибке
    def get_error_msg(self):
        msg = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.error_msg)))
        return msg.text

    # Заполнить все поля данными
    def fill_inputs_registraton(self, name=None, mail=None, password=None):
        if name is not None:
            self.write_in_field(self.user_name_input, name)
        if mail is not None:
            self.write_in_field(self.user_mail_input, mail)
        if password is not None:
            self.write_in_field(self.user_password_input, password)

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

    # Проверка сообщения об ошибке
    def assert_text_in_error(self, text):
        assert self.get_error_msg() == text

    def assert_input_name_is_not_empty(self):
        assert self.get_value(self.user_name_input) != 0