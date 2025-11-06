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




@allure.feature("Logo clicks")
class TestLogoClickFunctionality:
      
    
    @allure.title("Проверка перехода на нужную страницу при клике на лого Самокат")
    @allure.description("""
Цель теста: Проверить, что при клике на логотип 'Самокат' осуществляется переход на главную страницу сервиса.
""")
    
    # Проверка что при клике на логотип 'Самокат' осуществляется переход на главную страницу сервиса
    def test_click_logo_scooter_to_homepage(self, order_page):
        order_page.open()
        order_page.click_element(OrderLocators.SCOOTER_LOGO) #Клик по лого Самокат
        
        
        # Проверяем, что перешли на главную страницу сервиса Самокат
        assert order_page.current_url() == Data.STAND_URL, f"Expected {Data.STAND_URL}, but got {order_page.current_url()}"


    @allure.title("Проверка перехода на нужную страницу при клике на лого Яндекс")
    @allure.description("""
Цель теста: Проверить, что при клике на логотип 'Яндекс' осуществляется переход на главную страницу Дзена.  
""")
     # Проверка что при клике на логотип 'Яндекс' осуществляется переход на главную страницу Дзена
    def test_click_logo_yandex_to_homepage_dzen(self, order_page):
        order_page.open()
        order_page.click_element(OrderLocators.YANDEX_LOGO) #Клик по лого Яндекс
        
         # Ждем появления нового окна
        order_page.wait_for_new_window()

        # Переключаемся на новое окно
        order_page.switch_to_new_window()

        # Проверяем, что перешли на главную страницу Дзена
        assert Data.DZEN_URL in order_page.current_url(), f"Expected {Data.DZEN_URL}, but got {order_page.current_url()}"
   