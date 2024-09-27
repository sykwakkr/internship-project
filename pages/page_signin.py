from pages.page_base import PageBase
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from time import sleep


class PageSignin(PageBase):
    EMAIL_INPUT = (By.ID, 'email-2')
    PASSWORD_INPUT = (By.ID, 'field')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a.login-button.w-button')

    # Load the environment variables from the .env file
    load_dotenv()

    # Access variables using os.getenv()
    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')
    USER_COUNTER = (By.CSS_SELECTOR, 'div.number-text-grid.big')
    URL_LOGIN = 'sign-in'
    W_EL_TEXT = '-'
    BODY_PROPERTIES = 'body-properties'

    def log_in_to_the_page(self):
        self.wait_until_url_contains(self.URL_LOGIN)
        self.wait_until_not_text_present_element(self.W_EL_TEXT, *self.USER_COUNTER)
        self.input_text(self.EMAIL, *self.EMAIL_INPUT)
        self.input_text(self.PASSWORD, *self.PASSWORD_INPUT)
        self.click_element(*self.LOGIN_BUTTON)
        self.wait_until_body_change(self.BODY_PROPERTIES)
