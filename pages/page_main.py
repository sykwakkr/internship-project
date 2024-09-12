from pages.page_base import PageBase
from selenium.webdriver.common.by import By
from time import sleep


class PageMain(PageBase):
    REELLY_URL = 'https://soft.reelly.io'
    SETTINGS_BUTTON = (By.XPATH, '//div[contains(text(), "Settings")]')
    MOBILE_MAIN_MENU = (By.CSS_SELECTOR, 'a.assistant-button.w-inline-block')
    MENU_PHOTO_AVATAR = (By.CSS_SELECTOR, 'a.menu-photo_avatar.w-inline-block')
    USER_PROFILE_IMAGE = (By.CSS_SELECTOR, 'img[wized="userProfileImage"]')
    CARD_OF_PROPERTY = (By.CSS_SELECTOR, 'div[wized="projectsListing"] [w-list-index-value="0"]')

    def open_main_page(self):
        self.open_url(self.REELLY_URL)

    def click_settings(self, browser_mode):
        # TODO: Find out a solution for Safari at this step or more following steps
        if 'mobile' in browser_mode:
            self.click_element(*self.MOBILE_MAIN_MENU)
            self.click_element(*self.MENU_PHOTO_AVATAR)
        else:
            self.wait_until_all_visible_located(*self.CARD_OF_PROPERTY)
            self.click_element(*self.SETTINGS_BUTTON)

