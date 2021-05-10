import time
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage


def test_should_be_register_fields(browser):
    link = "https://4pda.ru/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.go_to_register_term()
    page.click_to_register_term()
    page.go_to_login_fields_page()
    page.should_be_login_field()
    page.should_be_pass_field()
    page.should_be_captcha()
    # page.go_to_register_term()
    # page.go_to_register_fields()
    # page.should_be_login_page()



