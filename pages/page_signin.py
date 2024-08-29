from pages.page_base import PageBase
from selenium.webdriver.common.by import By
from time import sleep


class PageSignin(PageBase):
    EMAIL_INPUT = (By.ID, 'email-2')
    PASSWORD_INPUT = (By.ID, 'field')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a.login-button.w-button')
    EMAIL = 's*******@gmail.com'
    PASSWORD = 'R*******'
    URL_SIGNIN = 'https://soft.reelly.io/sign-in'
    TITLE_SIGN_IN = 'Sign in'

    def log_in_to_the_page(self):
        self.wait_until_title_is(self.TITLE_SIGN_IN)
        self.driver.refresh()  # Workaround to avoid sleep(1) on Safari and Firefox
        self.input_text(self.EMAIL, *self.EMAIL_INPUT)
        self.input_text(self.PASSWORD, *self.PASSWORD_INPUT)
        self.click_element(*self.LOGIN_BUTTON)
