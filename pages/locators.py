from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    CART_PAGE_LINK = (By.CSS_SELECTOR, 'span.btn-group')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators:
    BUY_MORE_LINK = (By.CSS_SELECTOR, '#content_inner > p > a')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGICTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASS1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASS2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PREORDER_PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PREORDER_PRODUCT_NAME = (By.CSS_SELECTOR, 'div h1')
    PRODUCT_NAME_IN_BUSKET = (By.XPATH, '//div[@id="messages"]/div[1]/div/strong')
    PRODUCT_PRICE_IN_BUSKET = (By.XPATH, '//div[@id="messages"]/div[3]/div/p/strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')
