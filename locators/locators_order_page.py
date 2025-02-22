from selenium.webdriver.common.by import By

class OrderPageLocators:

    # всплывающие окна
    title_add_order = By.XPATH, '//div[text()="Заказ оформлен"]'
    title_confirmation_order = By.XPATH, '//div[text()="Хотите оформить заказ?"]'
    button_confirmation_order = By.XPATH, '//button[text()="Да"]'

    # окно информации аренды
    title_rent = By.XPATH, '//div[text()="Про аренду"]'
    list_count_rent_day = By.XPATH, '//div[@class="Dropdown-option" and text()="{}"]'
    checkbox_colour = By.XPATH, '//*[@id="{}"]'
    input_comment = By.XPATH, '//input[@placeholder = "Комментарий для курьера"]'
    input_date_rent = By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]'
    date_calendar_element = By.XPATH, '//*[contains(@class, "react-datepicker__day") and text()="{}"]'
    input_count_rent_day = By.XPATH, '//div[@class="Dropdown-placeholder" and text()="* Срок аренды"]'
    button_back = By.XPATH, '//button[text()="Назад"]'
    button_final_order = By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Заказать"]'

    # окно информации для клиент
    title_client = By.XPATH, '//div[text()="Для кого самокат"]'
    next_button = By.XPATH, '//button[text()="Далее"]'
    input_name_field = By.XPATH, '//input[@placeholder="* Имя"]'
    input_last_name_field = By.XPATH, '//input[@placeholder="* Фамилия"]'
    input_address_field = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    input_phone_field = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    input_metro_field = By.XPATH, '//input[@placeholder = "* Станция метро"]'
    metro_last_element_button = By.XPATH, '//*[contains(@class, "Order_Text") and text()="{}"]'
