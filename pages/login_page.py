from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'login is not presented in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'


    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "fakepass"
        email_adress = self.browser.find_element(By.CSS_SELECTOR, '#id_registration-email')
        email_adress.send_keys(email)
        password_1 = self.browser.find_element(By.CSS_SELECTOR, '#id_registration-password1')
        password_1.send_keys(password)
        password_2 = self.browser.find_element(By.CSS_SELECTOR, '#id_registration-password2')
        password_2.send_keys(password)
        button_registration = self.browser.find_element(By.CSS_SELECTOR, 'button[name="registration_submit"]')
        button_registration.click()