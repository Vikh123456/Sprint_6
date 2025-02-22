import allure

from locators.locators_main_page import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    # принимаем куки
    @allure.step('Принимаем Куки')
    def accept_cookie(self):
        return self.click_to_element(MainPageLocators.cookie_button)

    # кликаем по кнопке Заказать вверху страницы
    @allure.step('Кликаем по кнопке Заказать вверху страницы')
    def click_for_order_button_up(self):
        return self.click_to_element(MainPageLocators.order_up_button)

    # прокручиваем страницу вниз до кнопки Заказать
    @allure.step('Прокручиваем страницу вниз до кнопки Заказать')
    def scroll_for_order_button_down(self):
        button_order_finish = self.find_element_with_wait(MainPageLocators.order_down_button)
        self.scroll_for_element(button_order_finish)

    # кликаем по кнопке Заказать внизу страницы
    @allure.step('Кликаем по кнопке Заказать внизу страницы')
    def click_for_order_button_down(self):
        return self.click_to_element(MainPageLocators.order_down_button)

    # создание заказа
    def created_order(self, button):
        self.click_to_element(button)

    @allure.step('Прокручиваем страницу до последнего вопроса')
    def scroll_for_question_block(self):
        last_question = self.find_element_with_wait(MainPageLocators.question_scrool_locator)
        return self.scroll_for_element(last_question)

    # кликаем по стрелочке Вопроса
    @allure.step('Клик на Вопрос')
    def click_for_question (self, question_id):
        locator_question = self.format_locators(MainPageLocators.question_button, question_id)
        self.scroll_for_question_block()
        self.click_to_element(locator_question)

    @allure.step('Получение ответа на Вопрос')
    # получаем ответ на Вопрос
    def get_answer_text(self, question_id):
        locator_answer = self.format_locators(MainPageLocators.answer_button, question_id)
        self.scroll_for_question_block()
        return self.get_text_from_element(locator_answer)

    @allure.step('Проверяем ответ на Вопрос')
    # проверяем ответ Вопроса
    def check_answer_for_question(self, question_id):
        self.click_for_question(question_id)
        return self.get_answer_text(question_id)
