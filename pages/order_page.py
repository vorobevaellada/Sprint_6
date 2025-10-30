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
        return self  # Возвращаем self для цепочки вызовов (fluent interface)
    
    def enter_name(self, name):
        """
        Вводит имя пользователя
        Скрывает детали работы с полем
        """
        name_field = self._find_element(OrderLocators.NAME)
        name_field.clear()
        name_field.send_keys(name)
        return self
    
    def enter_surname(self, surname):
        """
        Вводит фамилию
        """
        surname_field = self._find_element(OrderLocators.SURNAME)
        surname_field.clear()
        surname_field.send_keys(surname)
        return self
    
    def enter_address(self, address):
        """
        Вводит адресс
        """
        address_field = self._find_element(OrderLocators.ADDRESS)
        address_field.clear()
        address_field.send_keys(address)
        return self
    
 #   def enter_metro(self, metro): # Это поле НЕ ввода, это выпадающий список
 #       """
 #       Вводит метро
 #       """
 #       metro_field = self._find_element(OrderLocators.METRO)
 #       metro_field.clear()
 #       metro_field.send_keys(metro)
 #       
 #       return self

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
        phone_field.clear()
        phone_field.send_keys(phone)
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
        when_to_deliver_field.clear()
        when_to_deliver_field.send_keys(when_to_deliver)
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
            self._find_element(OrderLocators.CHECK_STATUS)
            return True
        except Exception:
            return False


        
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
        return self
    
    
    
    def get_success_message(self):
        """
        Возвращает сообщение об успехе
        """
        return self._get_text(LoginPageLocators.SUCCESS_MESSAGE)
    
    def get_error_message(self):
        """
        Возвращает сообщение об ошибке
        """
        return self._get_text(LoginPageLocators.ERROR_MESSAGE)
    
    def is_login_successful(self):
        """
        Проверяет, что вход выполнен успешно
        Скрывает детали проверки от тестов
        """
        return self._is_element_present(LoginPageLocators.SUCCESS_MESSAGE)
    
    def is_error_displayed(self):
        """
        Проверяет, что отображается сообщение об ошибке
        """
        return self._is_element_present(LoginPageLocators.ERROR_MESSAGE)
    
    def clear_fields(self):
        """
        Очищает поля формы
        """
        username_field = self._find_element(LoginPageLocators.USERNAME_FIELD)
        password_field = self._find_element(LoginPageLocators.PASSWORD_FIELD)
        username_field.clear()
        password_field.clear()
        return self
