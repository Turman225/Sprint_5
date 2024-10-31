import time

import pytest

from pages.login_page import Login_page

url = 'https://stellarburgers.nomoreparties.site/'

@pytest.mark.parametrize('test_case', [1, 2 , 3, 4])
def test_login_page(driver, password, login, test_case):
    login_page = Login_page(driver, url)
    driver.get(url)
    match test_case:
        case 1:
            login_page.click_login_btn_in_home_page()
        case 2:
            login_page.click_user_acc_btn()
        case 3:
            login_page.click_user_acc_btn()
            login_page.click_registration_btn()
            login_page.click_login_btn()
        case 4:
            login_page.click_user_acc_btn()
            login_page.click_recover_password()
            login_page.click_login_btn()
    login_page.fill_inputs_login(login, password)
    login_page.click_login_btn()
    login_page.click_user_acc_btn()
    time.sleep(1)
    login_page.assert_successful_login("Turman")
    login_page.click_logout()
    time.sleep(1)
    driver.refresh()