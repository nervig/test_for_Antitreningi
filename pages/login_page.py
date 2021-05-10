from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_field()
        self.should_be_pass_field()

    def click_to_register_term(self):
        register_link = self.browser.find_element(*LoginPageLocators.REG_TERM_2)
        register_link.click()
        time.sleep(1)

    # def go_to_register_fields(self):
    #     reg_term_2 = self.browser.find_element(*LoginPageLocators.REG_TERM_2)
    #     reg_term_2.click()
    #     time.sleep(3)

    def should_be_login_field(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FIELD), "The login field is not exist"

    def should_be_pass_field(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD), "The password fields aren't exist"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD_2), "The password fields 2 aren't exist"

    def should_be_email_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_FIELD), "The email field is not exist"

    def should_be_captcha(self):
        assert self.is_element_present(*LoginPageLocators.CAPTCHA), "The captcha image is not show"
        assert self.is_element_present(*LoginPageLocators.CAPTCHA_REG), "The captcha field isn't ixist"