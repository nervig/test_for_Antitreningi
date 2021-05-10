import time

from .base_page import BasePage
from selenium.webdriver.common.by import By
# from .locators import MainPageLocators
# from .login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

# class MainPage(BasePage):
#     def go_to_login_page(self):
#         icon_login = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#         icon_login.click()
#         return LoginPage(browser=self.browser, url=self.browser.current_url)



# browser.get(link)
#     icon_login = browser.find_element_by_css_selector(".icon-login")
#     icon_login.click()
#     browser.implicitly_wait(10)
#     register_link = browser.find_element_by_css_selector("div.row.menu div.cell a")
#     register_link.click()
#     time.sleep(3)
#     reg_term_2 = browser.find_element_by_css_selector("#reg-term-2")
#     reg_term_2.click()
#     time.sleep(3)
#     submit_next = browser.find_element(By.XPATH, "//input[@type='submit' and @value='Далее']")
#     submit_next.click()
#     time.sleep(5)
