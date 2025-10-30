"""
Базовый класс для всех Page Object классов
Общая функциональность для работы со страницами
"""

from selenium.webdriver.support.ui import WebDriverWait # Класс ожидания, позволяющий ожидать появления определённых условий на странице (например, загрузки элемента).
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException # Исключение, которое возникает, если условие не выполняется в течение указанного времени ожидания.


class BasePage:
    """
    Базовый класс для всех страниц
    Содержит общие вспомогательные методы
    """
    
    def __init__(self, driver):
        """
        Хранит WebDriver внутри класса
        Внешний код не работает с драйвером напрямую
        """
        self._driver = driver  # Приватный атрибут
        self._wait = WebDriverWait(driver, 10) # для ожидания события (клика или поиска элемента)
    
    def _find_element(self, locator):
        """
        Вспомогательный метод поиска элемента
        Скрывает детали работы с WebDriver
        """
        # return self._wait.until(EC.presence_of_element_located(locator))
        return self._wait.until(EC.visibility_of_element_located(locator))
    
    def _find_clickable_element(self, locator):
        """
        Вспомогательный метод поиска кликабельного элемента
        """

        # может быть есть альтернативы element_to_be_clickable, более точные.
        return self._wait.until(EC.element_to_be_clickable(locator)) 
    
    def _get_text(self, locator):
        """
        Вспомогательный метод получения текста элемента
        """
        element = self._find_element(locator)
        return element.text
    
    def _is_element_present(self, locator, timeout=3):
        """
        Проверка наличия элемента
        """
        try:
            wait = WebDriverWait(self._driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def open_page(self, url):
        """
        Публичный метод открытия страницы
        Открывает указанный URL
        """
        self._driver.get(url)

    def scroll_down(self):
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")