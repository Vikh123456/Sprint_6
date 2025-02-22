import allure
import pytest

from data import comment
from tests.conftest import driver
from helpers import info_client, about_scooter_rent
from locators.locators_main_page import MainPageLocators


class TestOrderPage:
    @allure.step('Тестируем оформление заказа с валидными данными')
    @pytest.mark.parametrize('button',
                             [MainPageLocators.order_down_button,
                              MainPageLocators.order_up_button],
                             )
    def test_created_order(self, driver, button, main_page, order_page):
        main_page.accept_cookie()
        main_page.created_order(button)
        order_page.fill_form_about_info_client(
            name=info_client['name'],
            last_name=info_client['last_name'],
            address=info_client['address'],
            metro=info_client['metro'],
            phone=info_client['phone']
        )
        order_page.fill_form_about_rent(
            rent_day=about_scooter_rent['rent_day'],
            colour=about_scooter_rent['colour'],
            comment=comment
        )
        order_page.click_button_order_finall()
        order_page.confirmation_order()
        assert 'Заказ оформлен' in order_page.check_accept_order()
