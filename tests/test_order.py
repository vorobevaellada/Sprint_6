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
class TestOrder:
      
    
    @allure.title("Позитивный сценарий заказа самоката через кнопку в шапке сайта")
    @allure.description("Тест проверяет полный цикл оформления заказа самоката через кнопку Заказать в верхней части главной страницы. Используется номер телефона, начинающийся на цифру 8. После заполнения формы заказа ожидается появление окна подтверждения успешного создания заказа")
    
    # Проверка №1 с одним набором тестовых данных, где номер телефона пишем через "8", а заказ делаем через кнопку "Заказать" в хедере
    def test_order(self, order_page):
        order_page.open()
        # почему-то без скролла не работает (есть перекрывающие элементы)
        #order_page.click_element(MainPageLocators.COOKIE) # принимаем куки
        order_page.click_element(MainPageLocators.ORDER_BUTTON_HEADER) # клик по кнопке "Заказать" в хедере
        order_page.order(Test_Data.NAME, Test_Data.SURNAME, Test_Data.ADDRESS,Test_Data.METRO,Test_Data.PHONE,Test_Data.WHEN_TO_DELIVER )
        
        assert order_page.is_element_present(), f"Элемент {OrderLocators.CANCEL_THE_ORDER} отсутствует на странице."

        order_page.click_element(OrderLocators.SCOOTER_LOGO) # клик на лого самоката

        # Проверяем, что перешли обратно на главную страницу
        assert order_page.is_on_main_page(), f"Возврат на главную страницу ({Data.STAND_URL}) не выполнен. Текущий URL: {order_page.driver.current_url}"
    
        order_page._driver.back()
        order_page.click_element(OrderLocators.YANDEX_LOGO) # клик на лого Яндекса

        # Проверяем, что перешли на главную страницу Дзена
        assert order_page.is_on_main_page(), f"Возврат на главную страницу ({Data.DZEN_URL}) не выполнен. Текущий URL: {order_page.driver.current_url}"
    


   
    @allure.title("Позитивный сценарий заказа самоката через кнопку в футере сайта")
    @allure.description("Тест проверяет полноценный процесс оформления заказа самоката через кнопку Заказать в нижней части главной страницы. Используются альтернативные тестовые данные с номером телефона, начинающимся на +7. Завершается проверка появлением уведомления об успешной отправке заказа")

    # Проверка №2 с другим набором тестовых данных(где номер телефона пишем через "+7"),а заказ делаем через кнопку "Заказать" в футере
    def test_order_2(self, order_page):
        order_page.open()
        #order_page.click_element(MainPageLocators.COOKIE) # принимаем куки
        order_page.click_element(MainPageLocators.ORDER_BUTTON_FOOTER) # клик по кнопке "Заказать" в хедере
        order_page.order(Test_Data.NAME, Test_Data.SURNAME, Test_Data.ADDRESS,Test_Data.METRO,Test_Data.PHONE_NUMBER_WITH_PLUS_7,Test_Data.WHEN_TO_DELIVER )
        
        assert order_page.is_element_present(), f"Элемент {OrderLocators.CANCEL_THE_ORDER} отсутствует на странице."    
        
        order_page.click_element(OrderLocators.SCOOTER_LOGO) # клик на лого самоката

        # Проверяем, что перешли обратно на главную страницу
        assert order_page.is_on_main_page(), f"Возврат на главную страницу ({Data.STAND_URL}) не выполнен. Текущий URL: {order_page.driver.current_url}"
    
        order_page._driver.back()
        order_page.click_element(OrderLocators.YANDEX_LOGO) # клик на лого Яндекса

        # Проверяем, что перешли на главную страницу Дзена
        assert order_page.is_on_main_page(), f"Возврат на главную страницу ({Data.DZEN_URL}) не выполнен. Текущий URL: {order_page.driver.current_url}"
    

  
