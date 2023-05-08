import time

import pytest
from selenium import webdriver

from pages.locators import MainPageLocators
from pages.login_page import LoginPage


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    print('\n open browser....')
    print('\n login user....')
    page = LoginPage(browser, 'http://127.0.0.1:8000/user/login/')
    page.open()
    page.login_user('natediaz', 'humo6050')
    page.should_be_alert_success_message_on_main_page()
    yield browser
    print('\n quit browser....')
    browser.quit()