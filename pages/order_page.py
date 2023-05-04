import time

from pages.base_page import BasePage
from pages.locators import OrderPageLocators


class OrderPage(BasePage):
    def fill_out_the_order_form(self):
        self.browser.find_element(*OrderPageLocators.NAME).send_keys(time.time())
        self.browser.find_element(*OrderPageLocators.LASTNAME).send_keys(time.time())
        self.browser.find_element(*OrderPageLocators.EMAIL).send_keys(f'{time.time()}@mail.ru')
        self.browser.find_element(*OrderPageLocators.ADDRESS).send_keys('Bukhara Kagan')
        self.browser.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    def should_be_equals_order_product_and_main_page_product(self, h1):
        header_product = self.browser.find_element(*OrderPageLocators.ORDER_PRODUCT_HEADER).text
        assert h1 == header_product, 'Все плохо'