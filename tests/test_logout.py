import data as data
from pages.login_page import Login_page


class TestLogOutPage:
    def test_log_out(self, driver):
        logout_page = Login_page(driver, data.url)
        driver.get(data.url)
        logout_page.click_user_acc_btn()
        logout_page.fill_inputs_login(data.login, data.password)
        logout_page.click_login_btn()
        logout_page.click_user_acc_btn()
        logout_page.click_logout()
        logout_page.assert_url(f'{data.url}login')