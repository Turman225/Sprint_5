import time
from pages.login_page import Login_page

url = 'https://stellarburgers.nomoreparties.site/'

def test_log_out(driver, password, login):
    logout_page = Login_page(driver, url)
    driver.get(url)
    logout_page.click_user_acc_btn()
    logout_page.fill_inputs_login(login, password)
    logout_page.click_login_btn()
    logout_page.click_user_acc_btn()
    logout_page.click_logout()
    time.sleep(1)
    logout_page.assert_url(f'{url}login')