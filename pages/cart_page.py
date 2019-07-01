from .locators import CartPageLocators
from .base_page import BasePage


class CartPage(BasePage):
    def should_bee_empty_cart_page(self):
        assert self.is_element_present(*CartPageLocators.BUY_MORE_LINK),\
               'Busket is not empty'
