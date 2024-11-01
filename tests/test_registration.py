from pages.helpers import LogPass
import pages.data as data
from pages.registration_page import Registration_page

class TestRegistrationPage:
    def test_registration_fill_valid_data(self, driver):
        registration_page = Registration_page(driver, data.url)
        logpass = LogPass()
        driver.get(data.url)
        registration_page.click_user_acc_btn()
        registration_page.click_registration_btn()
        registration_page.fill_inputs_registraton('TEST', logpass.generate_mail(12), logpass.generate_secure_password(7))
        registration_page.assert_input_name_is_not_empty()
        registration_page.click_registration_btn()

    def test_registration_less_5_char_in_password_error(self, driver):
        registration_page = Registration_page(driver, data.url)
        logpass = LogPass()
        driver.get(data.url)
        registration_page.click_user_acc_btn()
        registration_page.click_registration_btn()
        registration_page.fill_inputs_registraton('TEST', logpass.generate_mail(12), logpass.generate_secure_password(5))
        registration_page.assert_input_name_is_not_empty()
        registration_page.click_registration_btn()
        registration_page.assert_text_in_error('Некорректный пароль')