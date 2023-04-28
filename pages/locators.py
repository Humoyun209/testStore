from selenium.webdriver.common.by import By


class WelcomePageLocators:
    # on mobile
    HAMBURGER_BTN = (By.CSS_SELECTOR, 'button.navbar-toggler')

    DROPDOWN_PROFILE = (By.CSS_SELECTOR, '.navbar-nav > li:last-child')
    LET_IS_GO_BTN = (By.CSS_SELECTOR, '.btn-lg')
    LOGIN_LINK = (By.CSS_SELECTOR, '.dropdown-menu li:last-child > a')
    REGISTER_LINK = (By.CSS_SELECTOR, '.dropdown-menu li:first-child > a')


class RegisterPageLocators:
    REGISTER_FORM = (By.XPATH, "//form[@method='post']")
    USERNAME = (By.NAME, 'username')
    FIRST_NAME = (By.NAME, 'first_name')
    LAST_NAME = (By.NAME, 'last_name')
    EMAIL = (By.NAME, 'email')
    PASSWORD1 = (By.NAME, 'password1')
    PASSWORD2 = (By.NAME, 'password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button.form-control')
    SUCCESS_ALERT_REGISTER = (By.CSS_SELECTOR, 'div.alert-success')


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "//form[@method='post']")
    USERNAME = (By.NAME, 'username')
    PASSWORD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.btn.btn-primary.form-control')
    SUCCESS_ALERT_LOGIN = (By.CSS_SELECTOR, 'div.alert-success')


class MainPageLocators:
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, '.col-xxl-4:nth-child(1) .btn')
    CATEGORIES = (By.CSS_SELECTOR, 'ul.list-group')