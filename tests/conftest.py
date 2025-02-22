import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.switch_page import SwitchPage


def pytest_addoption(parser):
    parser.addoption("--url", default='https://qa-scooter.praktikum-services.ru/')

@pytest.fixture()
def config(request):
    url = request.config.getoption("--url")
    return {"url": url}

@pytest.fixture()
def driver(config):
    driver = webdriver.Firefox()
    url = config.get("url")
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture()
def main_page(driver):
    return MainPage(driver)

@pytest.fixture()
def order_page(driver):
    return OrderPage(driver)

@pytest.fixture()
def switch_page(driver):
    return SwitchPage(driver)
