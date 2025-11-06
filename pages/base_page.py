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
        return self._wait.until(EC.visibility_of_element_located(locator))
    
    def _find_clickable_element(self, locator):
        """
        Вспомогательный метод поиска кликабельного элемента
        """

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


    def send(self, found_locator, text):
        found_locator.clear()
        found_locator.send_keys(text)
    

    
    def current_url(self):
        current_url = self._driver.current_url  # Обращаемся к водителю через _driver
        return current_url



    def wait_for_new_window(self, timeout=10):
        """
        Ждет появления нового окна
        """
        # Подождать, пока количество окон не станет равно 2
        WebDriverWait(self._driver, timeout).until(
            lambda driver: len(driver.window_handles) == 2
        )

    def switch_to_new_window(self):
        """
        Переключается на новое окно, отличающееся от оригинального
        """
        original_window = self._driver.current_window_handle

        # Находим новое окно
        for window_handle in self._driver.window_handles:
            if window_handle != original_window:
                self._driver.switch_to.window(window_handle)
                break
        
        WebDriverWait(self._driver, 10).until(
            lambda driver: driver.current_url != "about:blank" and driver.current_url != ""
        )