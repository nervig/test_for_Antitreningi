from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
from .locators import LoginPageLocators
import time


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_register_term(self):
        register_link = self.browser.find_element(*LoginPageLocators.REGISTER_LINK_TERM)
        register_link.click()
        time.sleep(1)

    def go_to_login_fields_page(self):
        link = self.browser.find_element(*BasePageLocators.SUBMIT_NEXT)
        link.click()
        time.sleep(1)