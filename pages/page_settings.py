from pages.page_base import PageBase
from selenium.webdriver.common.by import By
from time import sleep


class PageSettings(PageBase):
    DATA_PROFILE_SETTING = (By.CSS_SELECTOR, 'div.data-profile-setting')
    EDIT_PROFILE_BUTTON = (By.XPATH, '//div[text()="Edit profile"]')
    URL_SETTING = 'settings'

    def click_edit_profile(self):
        self.wait_until_url_contains(self.URL_SETTING)
        self.wait_until_all_visible_located(*self.DATA_PROFILE_SETTING)
        self.click_element(*self.EDIT_PROFILE_BUTTON)
