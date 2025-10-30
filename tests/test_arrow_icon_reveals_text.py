import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from data import Data
from data import Test_Data
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By

@allure.feature("Arrows")
class TestArrows:
    
    @pytest.fixture
    def main_page(self, driver):
        return MainPage(driver)
    
    @allure.title("Стрелки")
    @allure.description("Тест нажатия на стрелки с определенным текстом")
    def test_arrows(self, main_page):
        main_page.open()
        # почему-то без скролла не работает (есть перекрывающие элементы)
        
        main_page.click_element(MainPageLocators.COOKIE) # принимаем куки
        main_page.scroll_down() 
        for i in range(8):
            self.click_arrow(main_page, # ?
                            MainPageLocators.LOCATORS[i][0],
                            MainPageLocators.LOCATORS[i][1],
                            Test_Data.ARROWS_TEXT[i])

    # здесь title и description мы не пишем (надеюсь будет работать)
    def click_arrow(self, main_page, locator_click, locator_text, text):
        main_page.click_element(locator_click)
        found_text = main_page.get_arrow_text(locator_text) # найденный текст
        # может можно здесь добавить еще assert на проверку чего-нибудь, как в примерах 'example_page_object'
        assert found_text == text, f"Текст '{text}' не найден!"