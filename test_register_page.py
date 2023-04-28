import time

from pages.register_page import RegisterPage


def test_register_a_new_user(browser):
    page = RegisterPage(browser, 'http://80.249.147.135/user/register/')
    page.open()
    login = page.register_user()
    page.should_be_redirect_to_login_page()
    page.should_be_alert_success_message_on_login_page()
    return login