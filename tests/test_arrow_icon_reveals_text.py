import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from data import Data
from data import Test_Data
from locators.main_page_locators import MainPageLocators


# Параметры для тестов (локаторы и ожидаемые значения)
ARROW_TEST_DATA = [
    (MainPageLocators.LOCATORS[i][0], MainPageLocators.LOCATORS[i][1], Test_Data.ARROWS_TEXT[i]) 
    for i in range(len(MainPageLocators.LOCATORS))
]

@pytest.mark.parametrize('locator_click, locator_text, expected_text', ARROW_TEST_DATA)
@allure.feature("Arrows")
class TestArrows:
    
    
    
    @allure.title("Проверка открытия выпадающего списка вопросов о важном")
    @allure.description("Тест проверяет открытие выпадающих списков в разделе Вопросы о важном путем проверки отдельных элементов.")
    def test_arrows(self, main_page, locator_click, locator_text, expected_text):
        main_page.open()
        main_page.click_element(locator_click)
        actual_text = main_page.get_arrow_text(locator_text)
        
        assert actual_text == expected_text, f"Текст '{expected_text}' не соответствует ожидаемому значению."