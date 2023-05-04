from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WelcomePageLocators:
    # on mobile
    HAMBURGER_BTN = (By.CSS_SELECTOR, 'button.navbar-toggler')

    DROPDOWN_PROFILE = (By.CSS_SELECTOR, '.navbar-nav > li:last-child')
    LET_IS_GO_BTN = (By.CSS_SELECTOR, '.btn-lg')
    LOGIN_LINK = (By.CSS_SELECTOR, '.dropdown-menu li:last-child > a')
    REGISTER_LINK = (By.CSS_SELECTOR, '.dropdown-menu li:first-child > a')
    PROFILE_LINK = (By.CSS_SELECTOR, '.dropdown-menu li:first-child .dropdown-item')


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
    H1_PRODUCT = (By.CSS_SELECTOR, '.col-sm-8:first-child .card-title')


class ProfilePageLocators:
    USERNAME = (By.CSS_SELECTOR, '#id_username')
    EMAIL = (By.CSS_SELECTOR, '#id_email')
    PROFILE_IMAGE = (By.CSS_SELECTOR, '#id_image')
    CHANGE_BUTTON = (By.CSS_SELECTOR, '.btn-outline-primary')
    HEADER_PRODUCT = (By.CSS_SELECTOR, '.d-flex h5.text-primary')
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, 'button.w-100')
    IS_EMPTY = (By.CSS_SELECTOR, 'h3.mb-5')


class OrderPageLocators:
    NAME = (By.CSS_SELECTOR, '#id_first_name')
    LASTNAME = (By.CSS_SELECTOR, '#id_last_name')
    EMAIL = (By.CSS_SELECTOR, '#id_email')
    ADDRESS = (By.CSS_SELECTOR, '#id_address')
    ORDER_BUTTON = (By.CSS_SELECTOR, '.btn.w-100')
    ORDER_PRODUCT_HEADER = (By.CSS_SELECTOR, 'h5.text-primary')


class StripePageLocators:
    EMAIL = (By.CSS_SELECTOR, '#email')
    CARD = (By.CSS_SELECTOR, '#cardNumber')
    DATA = (By.CSS_SELECTOR, '#cardExpiry')
    CSV_CODE = (By.CSS_SELECTOR, '#cardCvc')
    BILLING_NAME = (By.CSS_SELECTOR, '#billingName')
    PAY_BUTTON = (By.CSS_SELECTOR, 'div.SubmitButton-IconContainer')
    SUCCESS_HEADER = (By.CSS_SELECTOR, 'h4.text-center')

    TEST_MAIL = 'h.ahmedov209@gmail.com'
    TEST_CARD_NUMBER = '42' * 8
    TEST_DATA = '1125'
    TEST_CSV_CODE = '111'
    TEST_FULL_NAME = 'Humoyun Ahmedov'
