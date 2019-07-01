from .base_page import BasePage
from .locators import ProductPageLocators


import time


class ProductPage(BasePage):

    def add_product_to_busket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def get_preorder_name(self):
        return self.browser.find_element(*ProductPageLocators.PREORDER_PRODUCT_NAME).text

    def get_preorder_price(self):
        return self.browser.find_element(*ProductPageLocators.PREORDER_PRODUCT_PRICE).text

    def get_order_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BUSKET).text

    def get_order_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BUSKET).text

    def should_be_right_name(self, order_name):
        preorder_name = self.get_preorder_name()
        assert preorder_name == order_name, "Product name doesn't match"

    def should_be_right_price(self, order_price):
        preorder_price = self.get_preorder_price()
        assert preorder_price == order_price, "Price doesn't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
               'Success message is present, but should bot be'

    def should_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
               'Message not disappeared, but should'
