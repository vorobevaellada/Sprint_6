"""
Page Object для Основной страницы
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage
from .main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.order_locators import OrderLocators
from data import Data
from data import Test_Data
from selenium.webdriver.support.ui import Select
import time
from urllib.parse import urlparse

class OrderPage(MainPage ):
    """
    Page Object для страницы Заказа
    Содержит методы для работы со страницей Заказа
    """
    
    def open(self):
        """
        Публичный метод открытия страницы Заказа
        Открывает нужный адрес
        """
        self.open_page(Data.ORDER_URL)
        self.click_element(MainPageLocators.COOKIE) # принимаем куки
        return self  # Возвращаем self для цепочки вызовов (fluent interface)
    
    def enter_name(self, name):
        """
        Вводит имя пользователя
        Скрывает детали работы с полем
        """
        name_field = self._find_element(OrderLocators.NAME)
        self.send(name_field, name)
        return self
    
    def enter_surname(self, surname):
        """
        Вводит фамилию
        """
        surname_field = self._find_element(OrderLocators.SURNAME)
        self.send(surname_field, surname)
        return self
    
    def enter_address(self, address):
        """
        Вводит адресс
        """
        address_field = self._find_element(OrderLocators.ADDRESS)
        self.send( address_field, address,)
        return self
    


    def enter_metro(self, metro):
        """
        Выбирает станцию метро из выпадающего списка
         """
        metro_field = self._find_element(OrderLocators.METRO)
        metro_field.click()  # Активируем поле для показа выпадающего списка
        selected_option = self._find_element(OrderLocators.METRO_CHERKIZOVSKAYA)
        selected_option.click()  # Выбираем пункт Черкизовская
        return self
    
    def enter_phone(self, phone):
        """
        Вводит телефон
        """
        phone_field = self._find_element(OrderLocators.PHONE)
        self.send(phone_field, phone)
        return self
    
     
    
    def click_next(self):
        """
        Нажимает кнопку Далее
        """
        next_button = self._find_clickable_element(OrderLocators.NEXT)
        next_button.click()
        return self
    
    def enter_when_to_deliver(self, when_to_deliver):
        """
        Вводит дату
        """
        when_to_deliver_field = self._find_element(OrderLocators.WHEN_TO_DELIVER)
        self.send(when_to_deliver_field,when_to_deliver )
        # Кликаем по элементу с нужной датой
        date_button = self._find_element(OrderLocators.WHEN_TO_DELIVER_CLICK)
        date_button.click()
        return self
    
    def enter_rental_term(self):
        """
        Выбирает Срок аренды из выпадающего списка
        """
        rental_term_field = self._find_element(OrderLocators.RENTAL_TERM)
        rental_term_field.click()  # Активируем поле для показа выпадающего списка
        rental_term_field = self._find_element(OrderLocators.RENTAL_TERM_TWO_DAYS)
        rental_term_field.click()  # Выбираем пункт Двое суток
        return self
    
    
    def enter_scooter_color(self):
        """
        Выбирает цвет самоката
        """
        scooter_color_field = self._find_element(OrderLocators.BLACK_SCOOTER)
        scooter_color_field.click()
        return self
    
    def click_submit_order(self):
        """
        Нажимает кнопку "Заказать" для завершения заказа
        """
        submit_order_field = self._find_element(OrderLocators.ORDER_BUTTON_IN_THE_ORDER)
        submit_order_field.click()
        return self
    
    def click_order_yes(self):
        """
        Нажимает кнопку "Заказать" для завершения заказа
        """
        submit_order_field = self._find_element(OrderLocators.ORDER_YES)
        submit_order_field.click()
        return self
    
    def is_element_present(self):
        """
        Проверяет присутствие элемента "Посмотреть статус заказа"
        Возвращает True, если элемент найден, иначе False
        """
        try:
            self._find_element(OrderLocators.CANCEL_THE_ORDER)
            return True
        except Exception:
            return False

    def click_check_status(self):
        """
        Нажимает кнопку "Посмотреть статус" и ждет 3 секунды после клика
        """
        time.sleep(3)  # Ждем 3 секунды, чтобы заказ успел сформироваться
        check_status_field = self._find_element(OrderLocators.CHECK_STATUS)
        check_status_field.click()
        time.sleep(3)  # Ждем 3 секунды после клика, чтобы обработка завершилась
        return self

        
    def order(self, name, surname, address, metro, phone, when_to_deliver):
        """
        Высокоуровневый метод логина
        Объединяет весь процесс входа в одном методе
        """
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_address(address)
        self.enter_metro(metro)
        self.enter_phone(phone)
        self.click_next()
        self.enter_when_to_deliver(when_to_deliver)
        self.enter_rental_term()
        self.enter_scooter_color()
        self.click_submit_order()
        self.click_order_yes()
        self.click_check_status()
        return self
    
    def is_on_main_page(self):
        """Проверяет, что текущая страница соответствует главной"""
        current_url = self._driver.current_url  # Обращаемся к водителю через _driver
        parsed_current_url = urlparse(current_url)
        parsed_stand_url = urlparse(Data.STAND_URL)
        return parsed_current_url.netloc == parsed_stand_url.netloc