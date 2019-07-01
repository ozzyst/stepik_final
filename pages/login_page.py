from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        register_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        register_email.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        password2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "It's not login url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
               'There is no login form on this page'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
               'There is no register form on this page'
