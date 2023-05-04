import time

import pytest

from pages.order_page import OrderPage
from pages.profile_page import ProfilePage
from pages.stripe_page import StripePage


@pytest.mark.pay
def test_fill_out_order_page_and_pay_on_stripe(browser):
    order_page = OrderPage(browser, 'http://127.0.0.1:8000/order')
    order_page.open()
    order_page.fill_out_the_order_form()
    stripe_page = StripePage(browser, browser.current_window_handle)
    stripe_page.fill_out_stripe_page()
    time.sleep(2)
    stripe_page.should_be_redirect_to_success_page()


@pytest.mark.pay
def test_check_good_must_be_disapper_after_purchase(browser):
    profile_page = ProfilePage(browser, 'http://127.0.0.1:8000/user/profile/6/')
    profile_page.open()
    profile_page.should_be_the_basket_is_empty_after_purchase()
