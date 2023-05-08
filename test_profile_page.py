import os
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.profile_page import ProfilePage
from pages.welcome_page import WelcomePage
from test_main_page import test_authorized_user_add_the_good_to_empty_basket


def test_change_field(browser):
    welcome_page = WelcomePage(browser, 'http://80.249.147.135/')
    welcome_page.go_to_profile()
    profile_page = ProfilePage(browser, 'http://80.249.147.135/user/profile/9/')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'files/test_image.jpeg')
    email = profile_page.set_email_and_image_on_profile(file_path)
    profile_page.should_be_modified_username_in_the_field_username(email)


@pytest.mark.add_to_basket
def test_add_to_empty_baket_and_check_product_on_order_page(browser):
    h1 = test_authorized_user_add_the_good_to_empty_basket(browser)
    main_page = MainPage(browser, 'http://127.0.0.1:8000/home')
    main_page.go_to_profile()
    profile_page = ProfilePage(browser, 'http://127.0.0.1:8000/user/profile/6/')
    profile_page.should_be_equals_products_main_page_and_profile_page(h1)
    profile_page.go_to_order_page()
    order_page = OrderPage(browser, 'http://127.0.0.1:8000/order/')
    order_page.should_be_equals_order_product_and_main_page_product(h1)

@pytest.mark.clean_basket
def test_clean_basket_after_adding_goods(browser):
    profile_page = ProfilePage(browser, 'http://127.0.0.1:8000/user/profile/6/')
    profile_page.open()
    profile_page.clear_basket()
    profile_page.should_be_success_message_after_cleaning()
    profile_page.should_be_the_basket_is_empty_after_cleaning()
