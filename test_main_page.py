import time

import pytest

from pages.main_page import MainPage
from pages.register_page import RegisterPage
from pages.welcome_page import WelcomePage
from test_login_page import test_login_an_existing_user

@pytest.mark.regression
def test_unauthorized_user_wants_to_add_the_good_to_the_basket(browser):
    page = MainPage(browser, 'http://80.249.147.135/home')
    page.open()
    page.add_to_the_basket()
    page.redirect_to_login_page_from_main_page_when_user_unauthorized()


@pytest.mark.smoke
def test_authorized_user_add_the_good_to_basket(browser):
    test_login_an_existing_user(browser)
    welcome_page = WelcomePage(browser, 'http://80.249.147.135/')
    welcome_page.go_to_catalogue()
    main_page = MainPage(browser, 'http://80.249.147.135/home/')
    main_page.add_to_the_basket()
    main_page.redirect_should_be_in_main_page_when_user_authorized()