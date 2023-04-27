from pages.locators import WelcomePageLocators, RegisterPageLocators
from pages.base_page import BasePage


class WelcomePage(BasePage):
    def go_to_register_on_pc(self):
        self.browser.find_element(*WelcomePageLocators.DROPDOWN_PROFILE).click()
        self.browser.find_element(*WelcomePageLocators.REGISTER_LINK).click()

    def go_to_register_on_mobile(self):
        self.browser.find_element(*WelcomePageLocators.HAMBURGER_BTN).click()
        self.browser.find_element(*WelcomePageLocators.DROPDOWN_PROFILE).click()
        self.browser.find_element(*WelcomePageLocators.REGISTER_LINK).click()

    def should_be_login_link(self):
        assert self.browser.find_element(*WelcomePageLocators.LOGIN_LINK), 'Log in link not found'

    def should_be_login_register(self):
        assert self.browser.find_element(*WelcomePageLocators.LOGIN_LINK), 'Register link not found'

    def shoule_be_register_form(self):
        assert self.browser.find_element(*RegisterPageLocators.FORM), 'Register link not found'