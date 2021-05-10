from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, ".icon-login")
    SUBMIT_NEXT = (By.XPATH, "//input[@type='submit' and @value='Далее']")

class LoginPageLocators():
    REGISTER_LINK_TERM = (By.CSS_SELECTOR, "div.row.menu div.cell a")
    REG_TERM_2 = (By.CSS_SELECTOR, "#reg-term-2")
    LOGIN_FIELD = (By.CSS_SELECTOR, "input[name='login']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    PASSWORD_FIELD_2 = (By.XPATH, "//input[@name='password2']")
    EMAIL_FIELD = (By.XPATH, "input[name='email']")
    CAPTCHA = (By.CSS_SELECTOR, "#reg-captcha-img")
    CAPTCHA_REG = (By.CSS_SELECTOR, "#reg-captcha")
