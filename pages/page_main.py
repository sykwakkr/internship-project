from pages.page_base import PageBase
from selenium.webdriver.common.by import By
from time import sleep


class PageMain(PageBase):
    REELLY_URL = 'https://soft.reelly.io'
    SETTINGS_BUTTON = (By.XPATH, '//div[contains(text(), "Settings")]')

    def open_main_page(self):
        self.open_url(self.REELLY_URL)

    def click_settings(self):
        settings_element = self.driver.find_elements(By.CSS_SELECTOR, '.menu-button-text')[17]
        print(settings_element.text)
        settings_element.click()
        self.click_element(*self.SETTINGS_BUTTON)

