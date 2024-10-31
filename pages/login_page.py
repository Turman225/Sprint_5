from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_model import Base_model
import json
from pathlib import Path

class Login_page(Base_model):

    input_user_login = '//input[@type="text"]' #Поле ввода логина
    input_user_password = '//input[@type="password"]'#Поле ввода пароля
    login_btn = "//*[text()='Войти']" #Кнопка войти
    recover_password = 'Восстановить пароль' #Кнопка восстановить пароль
    user_name = '//input[@name="Name"]' #Поле с именем в личном кабинете
    login_btn_in_home_page = '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]' #Кнопка авторизации в главном меню
    logout = '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]' #Кнопка выхода

    # Заполнить все поля данными
    def fill_inputs_login(self, mail=None, password=None):
        if mail is not None:
            self.write_in_field(self.input_user_login, mail)
        if password is not None:
            self.write_in_field(self.input_user_password, password)

    def click_login_btn(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_btn)))
        button.click()

    def click_login_btn_in_home_page(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_btn_in_home_page)))
        button.click()

    def click_recover_password(self):
        link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, self.recover_password)))
        link.click()

    def click_logout(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.logout)))
        button.click()

    def assert_successful_login(self, name):
        assert self.get_value(self.user_name) == name