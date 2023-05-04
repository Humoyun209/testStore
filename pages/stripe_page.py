import time

from pages.base_page import BasePage
from pages.locators import StripePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StripePage(BasePage):
    def fill_out_stripe_page(self):
        self.browser.find_element(*StripePageLocators.EMAIL).send_keys(StripePageLocators.TEST_MAIL)
        self.browser.find_element(*StripePageLocators.BILLING_NAME).send_keys(StripePageLocators.TEST_FULL_NAME)
        self.browser.find_element(*StripePageLocators.DATA).send_keys(StripePageLocators.TEST_DATA)
        self.browser.find_element(*StripePageLocators.CARD).send_keys(StripePageLocators.TEST_CARD_NUMBER)
        self.browser.find_element(*StripePageLocators.CSV_CODE).send_keys(StripePageLocators.TEST_CSV_CODE)
        self.browser.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)
        button = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(
            StripePageLocators.PAY_BUTTON
        ))
        button.click()

    def should_be_redirect_to_success_page(self):
        paid = self.browser.find_element(*StripePageLocators.SUCCESS_HEADER).text
        assert paid == 'Оплачена', 'Вы не вернулись в success page'