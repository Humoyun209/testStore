import time

from pages.base_page import BasePage
from pages.locators import ProfilePageLocators


class ProfilePage(BasePage):
    def set_email_and_image_on_profile(self, file_name):
        email = self.browser.find_element(*ProfilePageLocators.EMAIL)
        pr_image = self.browser.find_element(*ProfilePageLocators.PROFILE_IMAGE)
        btn = self.browser.find_element(*ProfilePageLocators.CHANGE_BUTTON)
        email.clear()
        email.send_keys(f'{time.time()}@yandex.ru')
        value = email.get_attribute('value')
        pr_image.send_keys(file_name)
        btn.click()
        return value

    def go_to_order_page(self):
        order_button = self.browser.find_element(*ProfilePageLocators.PLACE_ORDER_BUTTON)
        order_button.click()

    def should_be_equals_products_main_page_and_profile_page(self, header):
        header_text_on_profile = self.browser.find_element(*ProfilePageLocators.HEADER_PRODUCT).text
        assert header == header_text_on_profile, 'Продукт не тот продукт, который вы добавили.'

    def should_be_modified_username_in_the_field_username(self, email):
        new_email = self.browser.find_element(*ProfilePageLocators.EMAIL).get_attribute('value')
        assert new_email == email, 'Emails совпали'

    def should_be_the_basket_is_empty_after_purchase(self):
        txt = self.browser.find_element(*ProfilePageLocators.IS_EMPTY).text
        assert txt == 'BASKET EMPTY', 'Webhook еще не включен'