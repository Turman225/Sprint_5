from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_model import Base_model


class Homme_page(Base_model):
    buns = '//*[text()="Булки"]'
    souses = '//*[text()="Соусы"]'
    fillings = '//*[text()="Начинки"]'

    def click_buns(self):
        tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.buns)))
        tab.click()

    def click_souses(self):
        tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.souses)))
        tab.click()

    def click_fillings(self):
        tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.fillings)))
        tab.click()

    def assert_selected_tab(self, tab):
        selected_tab = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="{tab}"]')))
        assert selected_tab
