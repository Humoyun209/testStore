from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from test_register_page import test_register_a_new_user


def test_login_a_new_user(browser):
    page = RegisterPage(browser, 'http://80.249.147.135/user/register/')
    page.open()
    username, password = test_register_a_new_user(browser)
    page_login = LoginPage(browser, 'http://80.249.147.135/user/login/')
    page_login.login_user(username, password)
    page_login.should_be_alert_success_message_on_main_page()


def test_login_an_existing_user(browser):
    page = LoginPage(browser, 'http://127.0.0.1:8000/user/login/')
    page.open()
    page.login_user('natediaz', 'humo6050')
    page.should_be_alert_success_message_on_main_page()


