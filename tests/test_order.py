import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Data
from data import Test_Data
from locators.main_page_locators import MainPageLocators
from locators.order_locators import OrderLocators
from selenium.webdriver.common.by import By

@allure.feature("Order")
class TestArrows:
    
    @pytest.fixture
    def order_page(self, driver):
        return OrderPage(driver)
    
    @allure.title("Заказ самоката")
    @allure.description("Тест заказа самоката")
    
    # Проверка №1 с одним набором тестовых данных, где номер телефона пишем через "8", а заказ делаем через кнопку "Заказать" в хедере
    def test_order(self, order_page):
        order_page.open()
        # почему-то без скролла не работает (есть перекрывающие элементы)
        order_page.click_element(MainPageLocators.COOKIE) # принимаем куки
        order_page.click_element(MainPageLocators.ORDER_BUTTON_HEADER) # клик по кнопке "Заказать" в хедере
        order_page.order(Test_Data.NAME, Test_Data.SURNAME, Test_Data.ADDRESS,Test_Data.METRO,Test_Data.PHONE,Test_Data.WHEN_TO_DELIVER )
        
        assert order_page.is_element_present(), f"Элемент {OrderLocators.CHECK_STATUS} отсутствует на странице."

    # Проверка №2 с другим набором тестовых данных(где номер телефона пишем через "+7"),а заказ делаем через кнопку "Заказать" в футере
    def test_order_2(self, order_page):
        order_page.open()
        # почему-то без скролла не работает (есть перекрывающие элементы)
        order_page.click_element(MainPageLocators.COOKIE) # принимаем куки
        order_page.click_element(MainPageLocators.ORDER_BUTTON_FOOTER) # клик по кнопке "Заказать" в хедере
        order_page.order(Test_Data.NAME, Test_Data.SURNAME, Test_Data.ADDRESS,Test_Data.METRO,Test_Data.PHONE_NUMBER_WITH_PLUS_7,Test_Data.WHEN_TO_DELIVER )
        
        assert order_page.is_element_present(), f"Элемент {OrderLocators.CHECK_STATUS} отсутствует на странице."    



  
