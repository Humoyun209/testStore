from pages.authorization import TestUser
from pages.base_page import BasePage
from pages.locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):

    def login_user(self, username, password):
        self.browser.find_element(*LoginPageLocators.USERNAME).send_keys(username)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def should_be_alert_success_message_on_main_page(self):
        message = self.browser.find_element(*BasePageLocators.SUCCESS_MESSAGE)
        assert message.text == 'Вы успешно авторизовались', 'Авторизация не завершена'