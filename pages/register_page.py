import random
import time

from pages.authorization import TestUser
from pages.base_page import BasePage
from pages.locators import RegisterPageLocators, LoginPageLocators


class RegisterPage(BasePage):
    def register_user(self):
        u, p = TestUser.username, TestUser.password
        self.browser.find_element(*RegisterPageLocators.USERNAME).send_keys(u)
        self.browser.find_element(*RegisterPageLocators.FIRST_NAME).send_keys(TestUser.first_name)
        self.browser.find_element(*RegisterPageLocators.LAST_NAME).send_keys(TestUser.last_name)
        self.browser.find_element(*RegisterPageLocators.EMAIL).send_keys(TestUser.email)
        self.browser.find_element(*RegisterPageLocators.PASSWORD1).send_keys(p)
        self.browser.find_element(*RegisterPageLocators.PASSWORD2).send_keys(p)

        self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        return u, p

    def should_be_redirect_to_login_page(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), 'Регистрация не завершена'

    def should_be_alert_success_message_on_login_page(self):
        message = self.browser.find_element(*RegisterPageLocators.SUCCESS_ALERT_REGISTER)
        assert message.text == 'Вы успешно зарегистртровались', 'Регистрация не завершена'