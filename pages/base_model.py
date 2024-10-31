from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import json
from pathlib import Path

class Base_model():

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    user_account = "//*[text()='Личный Кабинет']"#Кнопка "личный кабинет"
    registration_btn = "//*[text()='Зарегистрироваться']" #Кнопка "зарегистрироваться"
    designer = "//*[text()='Конструктор']" #Кнопка "конструктор"
    logo = '//a[@href="/"]'

    def click_user_acc_btn(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_account)))
        button.click()

    def click_registration_btn(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.registration_btn)))
        button.click()

    def click_designer(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.designer)))
        button.click()

    def click_logo(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.logo)))
        button.click()

    # Заполняем нужное поле
    def write_in_field(self, input=None, text=None):
        field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, input)))
        field.send_keys(text)

    def get_value(self, locator):
        elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return elem.get_attribute('value')

    def assert_url(self, url):
        assert self.driver.current_url == url