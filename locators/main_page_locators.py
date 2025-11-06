"""
Локаторы для главной страници
"""

from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Локаторы для главной страници
    """
    COOKIE = (By.XPATH, "//*[@id='rcc-confirm-button']") # куки

    HOW_MUCH_AND_PAY_DROPDOWN = (By.XPATH, "//*[@id='accordion__heading-0']")  # Стрелочка 1 "Сколько стоит? И как оплатить?"
    TEXT_HOW_MUCH_AND_PAY_DROPDOWN = (By.XPATH, "//*[@id='accordion__panel-0']")

    MULTIPLE_SCOOTERS_REQUEST = (By.XPATH, "//*[@id='accordion__heading-1']") # Стрелочка 2 "Хочу сразу несколько самокатов! Так можно?"
    TEXT_MULTIPLE_SCOOTERS_REQUEST = (By.XPATH, "//*[@id='accordion__panel-1']")
    
    HOW_RENTAL_TIME_IS_CALCULATED = (By.XPATH, "//*[@id='accordion__heading-2']") # Стрелочка 3 "Как рассчитывается время аренды?"
    TEXT_HOW_RENTAL_TIME_IS_CALCULATED = (By.XPATH, "//*[@id='accordion__panel-2']")
    
    SAME_DAY_SCOOTER_BOOKING = (By.XPATH, "//*[@id='accordion__heading-3']") # Стрелочка 4 "Можно ли заказать самокат прямо на сегодня?"
    TEXT_SAME_DAY_SCOOTER_BOOKING = (By.XPATH, "//*[@id='accordion__panel-3']")
    
    EXTEND_OR_RETURN_EARLY_OPTION = (By.XPATH, "//*[@id='accordion__heading-4']") # Стрелочка 5 "Можно ли продлить заказ или вернуть самокат раньше?"
    TEXT_EXTEND_OR_RETURN_EARLY_OPTION = (By.XPATH, "//*[@id='accordion__panel-4']")
    
    CHARGER_INCLUSION_CONFIRMATION = (By.XPATH, "//*[@id='accordion__heading-5']") # Стрелочка 6 "Вы привозите зарядку вместе с самокатом?"
    TEXT_CHARGER_INCLUSION_CONFIRMATION = (By.XPATH, "//*[@id='accordion__panel-5']")
    
    ORDER_CANCELLATION_OPTION = (By.XPATH, "//*[@id='accordion__heading-6']") # Стрелочка 7 "Можно ли отменить заказ?"
    TEXT_ORDER_CANCELLATION_OPTION = (By.XPATH, "//*[@id='accordion__panel-6']")

    DELIVERY_OUTSIDE_MKAD = (By.XPATH, "//*[@id='accordion__heading-7']") # Стрелочка 8 "Я жизу за МКАДом, привезёте?"
    TEXT_ELIVERY_OUTSIDE_MKAD = (By.XPATH, "//*[@id='accordion__panel-7']")

    ORDER_BUTTON_HEADER = (By.XPATH, "//*[@class='Button_Button__ra12g']") # Кнопка "Заказать" в хедере
    ORDER_BUTTON_FOOTER = (By.XPATH, "//*[@class='Button_Button__ra12g Button_Middle__1CSJM']") # Кнопка "Заказать" в футере

    LOCATORS = [(HOW_MUCH_AND_PAY_DROPDOWN, TEXT_HOW_MUCH_AND_PAY_DROPDOWN),
                (MULTIPLE_SCOOTERS_REQUEST, TEXT_MULTIPLE_SCOOTERS_REQUEST),
                (HOW_RENTAL_TIME_IS_CALCULATED, TEXT_HOW_RENTAL_TIME_IS_CALCULATED),
                (SAME_DAY_SCOOTER_BOOKING, TEXT_SAME_DAY_SCOOTER_BOOKING),
                (EXTEND_OR_RETURN_EARLY_OPTION, TEXT_EXTEND_OR_RETURN_EARLY_OPTION),
                (CHARGER_INCLUSION_CONFIRMATION, TEXT_CHARGER_INCLUSION_CONFIRMATION),
                (ORDER_CANCELLATION_OPTION, TEXT_ORDER_CANCELLATION_OPTION),
                (DELIVERY_OUTSIDE_MKAD, TEXT_ELIVERY_OUTSIDE_MKAD)]
