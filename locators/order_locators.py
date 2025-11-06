"""
Локаторы для страници Заказа
"""

from selenium.webdriver.common.by import By


class OrderLocators:
    """
    Локаторы для главной страници
    """
    NAME = (By.XPATH, '//*[@placeholder="* Имя"]') 
    
    SURNAME = (By.XPATH, '//*[@placeholder="* Фамилия"]') 

    ADDRESS = (By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]') 

    METRO = (By.XPATH, '//*[@placeholder="* Станция метро"]') # Выпадающее меню

    PHONE = (By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]')

    NEXT = (By.XPATH, '//*[@class="Button_Button__ra12g Button_Middle__1CSJM"]')

    METRO_CHERKIZOVSKAYA = (By.XPATH, '//div[text()="Черкизовская"]/parent::button')

    WHEN_TO_DELIVER = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]') # Локатор поля "Дата"
    WHEN_TO_DELIVER_CLICK = (By.XPATH, '//*[@aria-label="Choose четверг, 1-е января 2026 г."]') # Локатор конкретной даты

    RENTAL_TERM = (By.XPATH, '//*[@class="Dropdown-placeholder"]')

    RENTAL_TERM_TWO_DAYS = (By.XPATH, '//*[contains(@class, "Dropdown-option")][text()="двое суток"]')

    BLACK_SCOOTER = (By.XPATH, '//*[@for="black"]') # Локатр выбора черного самоката

    ORDER_BUTTON_IN_THE_ORDER = (By.XPATH, '//*[@class="Button_Button__ra12g Button_Middle__1CSJM"]') # Кнопка "Заказать" при вводе всех данных в форму заказа
    ORDER_YES = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']") # Кнопка "Да"

    CHECK_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']") # Кнопка "Посмотреть статус"

    CANCEL_THE_ORDER = (By.XPATH, "//button[.='Отменить заказ']")

    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']") # Лого Самоката

    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']") # Лого Яндекса

    ORDER_CONFIRMED =(By.XPATH, "//*[contains(text(), 'Заказ оформлен')]") # локатр с текстом Заказ оформлен, который появляется после оформления Заказа