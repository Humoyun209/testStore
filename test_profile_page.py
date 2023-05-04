import os
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.profile_page import ProfilePage
from pages.welcome_page import WelcomePage


def test_change_field(browser):
    welcome_page = WelcomePage(browser, 'http://80.249.147.135/')
    welcome_page.go_to_profile()
    profile_page = ProfilePage(browser, 'http://80.249.147.135/user/profile/9/')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'files/test_image.jpeg')
    email = profile_page.set_email_and_image_on_profile(file_path)
    profile_page.should_be_modified_username_in_the_field_username(email)


def test_place_orders(browser):
    welcome_page = WelcomePage(browser, 'http://127.0.0.1:8000/')
    welcome_page.go_to_catalogue()
    main_page = MainPage(browser, 'http://127.0.0.1:8000/home')
    h1 = main_page.add_to_the_basket()
    main_page = MainPage(browser, 'http://127.0.0.1:8000/home')
    main_page.go_to_profile()
    profile_page = ProfilePage(browser, 'http://127.0.0.1:8000/profile/6/')
    profile_page.should_be_equals_products_main_page_and_profile_page(h1)
    profile_page.go_to_order_page()
    order_page = OrderPage(browser, 'http://127.0.0.1:8000/order/')
    order_page.should_be_equals_order_product_and_main_page_product(h1)