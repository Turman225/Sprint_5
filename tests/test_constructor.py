import time

import pytest

from pages.home_page import Homme_page

url = 'https://stellarburgers.nomoreparties.site/'

@pytest.mark.parametrize('tab', ['Соусы', 'Начинки', 'Булки'])
def test_constructor(driver, tab):
    constructor_model = Homme_page(driver, url)
    driver.get(url)
    match tab:
        case 'Булки':
            constructor_model.click_souses()
            constructor_model.click_buns()
        case 'Соусы':
            constructor_model.click_souses()
        case 'Начинки':
            constructor_model.click_fillings()
    time.sleep(1)
    constructor_model.assert_selected_tab(tab)