from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import pytest
import time


class TestUserAddToCartFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.browser = browser
        link = 'http://selenium1py.pythonanywhere.com/'
        register_page = LoginPage(self.browser, link)
        register_page.open()
        register_page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = 'A#1234567z'
        register_page.register_new_user(email, password)
        register_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/'\
               'the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(self.browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/'\
               'the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(self.browser, link)
        page.open()
        page.add_product_to_busket()
        order_name = page.get_order_name()
        page.should_be_right_name(order_name)
        order_price = page.get_order_price()
        page.should_be_right_price(order_price)


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/'\
           'the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_busket()
    order_name = page.get_order_name()
    page.should_be_right_name(order_name)
    order_price = page.get_order_price()
    page.should_be_right_price(order_price)


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/'\
           'the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = link = 'http://selenium1py.pythonanywhere.com/catalogue/'\
                  'the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/'\
           'the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/'\
           'the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_bee_empty_cart_page()
