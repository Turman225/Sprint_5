import time

import pytest

from pages.registration_page import Registration_page

url = 'https://stellarburgers.nomoreparties.site/'

@pytest.mark.parametrize('length', [7, 5])
def test_registration(driver, length):
    registration_page = Registration_page(driver, url)
    driver.get(url)
    registration_page.click_user_acc_btn()
    registration_page.click_registration_btn()
    if length == 7:
        registration_page.fill_inputs_registraton('TEST', registration_page.generate_mail(12), registration_page.generate_secure_password(length))
        registration_page.assert_input_name_is_not_empty()
        registration_page.click_registration_btn()
    else:
        registration_page.fill_inputs_registraton('TEST', registration_page.generate_mail(12), registration_page.generate_secure_password(length))
        registration_page.assert_input_name_is_not_empty()
        registration_page.click_registration_btn()
        registration_page.assert_text_in_error('Некорректный пароль')

