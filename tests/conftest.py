import pytest
from selenium import webdriver
import pages.data as log_pass

@pytest.fixture(scope='module')
def driver():
    # Инициализация браузера
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Передача браузера в тесты
    yield driver
    # Закрытие браузера после завершения всех тестов
    driver.quit()

@pytest.fixture(scope='module')
def login():
    return log_pass.login

@pytest.fixture(scope='module')
def password():
    return log_pass.password