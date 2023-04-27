from selenium.webdriver.common.by import By


class WelcomePageLocators:
    # on mobile
    HAMBURGER_BTN = (By.CSS_SELECTOR, 'button.navbar-toggler')

    DROPDOWN_PROFILE = (By.CSS_SELECTOR, '.navbar-nav > li:last-child')
    LET_IS_GO_BTN = (By.CSS_SELECTOR, '.btn-lg')
    LOGIN_LINK = (By.CSS_SELECTOR, '.dropdown-menu li:last-child > a')
    REGISTER_LINK = (By.CSS_SELECTOR, '.dropdown-menu li:first-child > a')


class RegisterPageLocators:
    FORM = (By.XPATH, "//form[@method='post']")