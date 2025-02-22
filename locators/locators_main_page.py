from selenium.webdriver.common.by import By

class MainPageLocators:

    order_up_button = By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[@class="Button_Button__ra12g" and text()="Заказать"]'
    order_down_button = By.XPATH, '//button[contains(@class, "Button_Middle") and text() = "Заказать"]'
    cookie_button = By.ID, 'rcc-confirm-button'
    answer_button = By.XPATH, '//div[@id="accordion__panel-{}"]/p'
    question_scrool_locator = By.XPATH, '//div[@id="accordion__heading-7"]'
    question_button = By.XPATH, '//div[@id="accordion__heading-{}"]'
