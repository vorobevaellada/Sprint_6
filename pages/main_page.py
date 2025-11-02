"""
Page Object для Основной страницы
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import Data
from data import Test_Data


class MainPage(BasePage):
    """
    Page Object для Основной страницы
    Содержит методы для работы с Основной страницей
    """

    def open(self):
        """
        Публичный метод открытия Главной страницы
        Открывает нужный адрес
        """
        self.open_page(Data.STAND_URL)
        self.click_element(MainPageLocators.COOKIE) # принимаем куки
        self.scroll_down() 

        return self  # Возвращаем self для цепочки вызовов (fluent interface)
    
    
    def click_element(self, locator):
        """
        Нажимает на элемент
        (Возможно можно перенести этот метод в base_page)
        """
        arrow_button = self._find_clickable_element(locator)
        arrow_button.click()
        
    
    def get_arrow_text(self, locator):
        """
        Возвращает текст соответствующий вопросу данной стрелочки
        """
        arrow = self._find_element(locator)
        return arrow.text
    
    def verify_arrow_text(self, locator, expected_text):
       """
       Проверяет текст стрелочки, сравнивая его с ожидаемым значением
       """
       actual_text = self.get_arrow_text(locator)
       assert actual_text == expected_text, f"Text mismatch: Expected '{expected_text}', but got '{actual_text}'"
    