from pages.page_base import PageBase
from selenium.webdriver.common.by import By
from time import sleep


class PageSettings(PageBase):
    DATA_PROFILE_SETTING = (By.CSS_SELECTOR, 'div.data-profile-setting')
    EDIT_PROFILE_BUTTON = (By.XPATH, '//div[text()="Edit profile"]')
    URL_SETTING = 'settings'
    PARTIAL_USER_NAME = 'test+justin+careerist'
    PAGE_SETTING_BLOCK = (By.CSS_SELECTOR, 'a.page-setting-block.w-inline-block')
    BUTTON_LINK_MENU = (By.CSS_SELECTOR, 'a.button-link-menu.w-inline-block')
    TAG_BODY = (By.TAG_NAME, 'body')
    BODY_PROFILE = 'body-profile'
    BODY_SETTING = 'body-setting'

    def verify_settings_page_open(self, url_page):
        self.wait_until_url_contains(url_page)
        self.wait_until_all_visible_located(*self.DATA_PROFILE_SETTING)
        body_setting = self.find_elements(*self.TAG_BODY)[0].get_attribute('class')
        assert body_setting == self.BODY_SETTING, f'Expected Body class name {self.BODY_SETTING}, got {body_setting}'

    def click_edit_profile(self):
        url_page = self.URL_SETTING
        self.verify_settings_page_open(url_page)
        self.click_element(*self.EDIT_PROFILE_BUTTON)
        self.wait_until_body_change(self.BODY_PROFILE)

    def verify_settings_options(self, number_of_options):
        expected_number_of_options = number_of_options
        actual_number_of_options = str(len(self.find_elements(*self.PAGE_SETTING_BLOCK)))
        assert actual_number_of_options == expected_number_of_options, f'Expected {expected_number_of_options} options, got {actual_number_of_options}'

    def verify_option_button(self, option, browser_mode):
        expected_option_name = option
        if 'mobile' in browser_mode:
            actual_text = self.find_elements(*self.BUTTON_LINK_MENU)[1].text
        else:
            actual_text = self.find_elements(*self.BUTTON_LINK_MENU)[0].text
        assert actual_text == expected_option_name, f'Expected {expected_option_name} to be {actual_text}'
