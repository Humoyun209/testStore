import time

from pages.base_page import BasePage
from pages.locators import MainPageLocators, LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def add_to_the_basket(self):
        button = self.browser.find_element(*MainPageLocators.ADD_BASKET_BUTTON)
        self.browser.execute_script("window.scrollBy(0, 500);")
        time.sleep(5)
        button.click()

    def redirect_should_be_in_main_page_when_user_authorized(self):
        self.browser.find_element(*MainPageLocators.CATEGORIES), 'Ошибка при добавлении в корзину'

    def redirect_to_login_page_from_main_page_when_user_unauthorized(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), 'Пользователь зарегистрирован'