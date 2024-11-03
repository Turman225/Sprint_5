import data as data
import pytest
from pages.home_page import Homme_page


class TestConstructor:
    @pytest.mark.parametrize('tab', ['Соусы', 'Начинки', 'Булки'])
    def test_constructor(self, driver, tab):
        constructor_model = Homme_page(driver, data.url)
        driver.get(data.url)

        match tab:
            case 'Булки':
                constructor_model.click_souses()
                constructor_model.click_buns()
            case 'Соусы':
                constructor_model.click_souses()
            case 'Начинки':
                constructor_model.click_fillings()

        constructor_model.assert_selected_tab(tab)
