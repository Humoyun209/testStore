from pages.authorization import TestUser
from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def login_user_came_from_registration_page(self, username, password):
        self.browser.find_element(*LoginPageLocators.USERNAME).send_keys(username)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def should_be_alert_success_message_on_main_page(self):
        message = self.browser.find_element(*LoginPageLocators.SUCCESS_ALERT_LOGIN)
        assert message.text == 'Вы успешно авторизовались', 'Авторизация не завершена'