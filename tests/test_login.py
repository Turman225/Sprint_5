import pytest
import data as data
from pages.login_page import Login_page


class TestLoginPage:
    @pytest.mark.parametrize('test_case', [1, 2 , 3, 4])
    def test_login_page(self, driver, test_case):
        login_page = Login_page(driver, data.url)
        driver.get(data.url)
        match test_case:
            case 1:
                login_page.click_login_btn_in_home_page()
            case 2:
                login_page.click_user_acc_btn()
                login_page.click_logout()
            case 3:
                login_page.click_user_acc_btn()
                login_page.click_logout()
                login_page.click_registration_btn()
                login_page.click_login_btn()
            case 4:
                login_page.click_user_acc_btn()
                login_page.click_logout()
                login_page.click_recover_password()
                login_page.click_login_btn()
        login_page.fill_inputs_login(data.login, data.password)
        login_page.click_login_btn()
        login_page.click_user_acc_btn()
        login_page.assert_successful_login("Turman")
