import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.main_page import MainPage  # добавляем сюда импорт страницы!
from pages.order_page import OrderPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    yield driver
    #driver.quit() # закомментировать, если хочется чтобы браузер не закрывался

@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def order_page(driver):
    return OrderPage(driver)


