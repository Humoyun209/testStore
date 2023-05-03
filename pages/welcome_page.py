from pages.locators import WelcomePageLocators, RegisterPageLocators, MainPageLocators
from pages.base_page import BasePage


class WelcomePage(BasePage):
    def go_to_register_on_pc(self):
        self.browser.find_element(*WelcomePageLocators.DROPDOWN_PROFILE).click()
        self.browser.find_element(*WelcomePageLocators.REGISTER_LINK).click()

    def go_to_register_on_mobile(self):
        self.browser.find_element(*WelcomePageLocators.HAMBURGER_BTN).click()
        self.browser.find_element(*WelcomePageLocators.DROPDOWN_PROFILE).click()
        self.browser.find_element(*WelcomePageLocators.REGISTER_LINK).click()

    def go_to_catalogue(self):
        self.browser.find_element(*WelcomePageLocators.LET_IS_GO_BTN).click()
        list_cats = self.browser.find_element(*MainPageLocators.CATEGORIES)
        assert bool(list_cats), 'Переход был не успешно'

    def should_be_login_link(self):
        assert self.browser.find_element(*WelcomePageLocators.LOGIN_LINK), 'Log in link not found'

    def should_be_register_link(self):
        assert self.browser.find_element(*WelcomePageLocators.REGISTER_LINK), 'Register link not found'

    def should_be_register_form(self):
        assert self.browser.find_element(*RegisterPageLocators.REGISTER_FORM), 'Register link not found'

    def go_to_profile(self):
        self.browser.find_element(*WelcomePageLocators.HAMBURGER_BTN).click()
        self.browser.find_element(*WelcomePageLocators.DROPDOWN_PROFILE).click()
        self.browser.find_element(*WelcomePageLocators.PROFILE_LINK).click()