from pages.page_base import PageBase
from selenium.webdriver.common.by import By
from time import sleep


class PageSettings(PageBase):
    EDIT_PROFILE_BUTTON = (By.XPATH, '//div[text()="Edit profile"]')
    DATA_PROFILE_SETTING = (By.CSS_SELECTOR, '.data-profile-setting')

    def click_edit_profile(self):
        self.wait_until_all_visible(*self.DATA_PROFILE_SETTING)
        self.click_element(*self.EDIT_PROFILE_BUTTON)