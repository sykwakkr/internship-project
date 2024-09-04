from pages.page_base import PageBase
from selenium.webdriver.common.by import By
from time import sleep


class PageMain(PageBase):
    REELLY_URL = 'https://soft.reelly.io'
    SETTINGS_BUTTON = (By.XPATH, '//div[contains(text(), "Settings")]')
    CARD_OF_PROPERTY = (By.CSS_SELECTOR, 'div[wized="projectsListing"] [w-list-index-value="0"]')

    def open_main_page(self):
        self.open_url(self.REELLY_URL)

    def click_settings(self):
        # TODO: Find out a solution for Safari at this step or more following steps
        self.wait_until_all_visible_located(*self.CARD_OF_PROPERTY)
        self.click_element(*self.SETTINGS_BUTTON)

