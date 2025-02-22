import allure

from tests.conftest import driver


class TestSwitchPage:
    @allure.title('Проверка перехода на главную страницу по клику на лого Самоката')
    def test_transition_from_order_page_to_main_page(self, switch_page, main_page):
        main_page.accept_cookie()
        main_page.click_for_order_button_up()
        switch_page.switch_to_scooter_page()
        assert 'Самокат' in switch_page.get_scooter_headline_text()

    @allure.title('Проверка перехода на Дзен по клику на лого Дзена')
    def test_transition_from_order_page_to_dzen(self, driver, switch_page, main_page):
        main_page.accept_cookie()
        switch_page.switch_to_dzen_page()
        assert switch_page.check_dzen_button()
