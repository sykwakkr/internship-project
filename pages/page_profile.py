from pages.page_base import PageBase
from selenium.webdriver.common.by import By
from time import sleep


class PageProfile(PageBase):
    JOINED_INPUT_PROFILE = (By.ID, 'When-joined-company-2')
    JOINED_INPUT = '2024 Q2'
    LANGUAGE_INPUT_PROFILE = (By.ID, 'Languages')
    LANGUAGE_INPUT = 'English'
    ROLE_INPUT_PROFILE = (By.ID, 'field')
    ROLE_INPUT = 'Developer'
    CLOSE_BUTTON_PROFILE = (By.CSS_SELECTOR, '.close-button.w-button')
    SAVE_BUTTON_PROFILE = (By.CSS_SELECTOR, '.save-changes-button')
    BUTTON_PROFILE = (By.CSS_SELECTOR, '.button-profile .save-changes-button')
    JOINED_INPUT_PROFILE_VALUE = 'undefined'
    USER_UPLOADED_IMAGE = (By.CSS_SELECTOR, 'img[wized="userUploadedImage"]')
    URL_PROFILE_EDIT = 'profile-edit'
    PROFILE_BUTTON_SAVE_BLOCK = (By.CSS_SELECTOR, 'div.profile-button-block .save-changes-button')
    PROFILE_BUTTON_SAVE = (By.CSS_SELECTOR, 'div.profile-button .save-changes-button')
    PROFILE_BUTTON_CLOSE_BLOCK = (By.CSS_SELECTOR, 'div.profile-button-block .close-button.w-button')
    PROFILE_BUTTON_CLOSE = (By.CSS_SELECTOR, 'div.profile-button .close-button.w-button')

    def enter_test_info_input_fields(self):
        self.wait_until_all_visible_located(*self.USER_UPLOADED_IMAGE)
        self.wait_until_not_text_present_element_value(self.JOINED_INPUT_PROFILE_VALUE, *self.JOINED_INPUT_PROFILE)
        cur_joined_value = self.driver.find_element(*self.JOINED_INPUT_PROFILE).get_attribute('value')  # To avoid from appending input values to existing value
        self.wait_until_text_present_element_value(cur_joined_value, *self.JOINED_INPUT_PROFILE)
        self.clear_text(*self.JOINED_INPUT_PROFILE)
        self.input_text(self.JOINED_INPUT, *self.JOINED_INPUT_PROFILE)
        self.wait_until_text_present_element_value(self.JOINED_INPUT, *self.JOINED_INPUT_PROFILE)
        self.input_text(self.LANGUAGE_INPUT, *self.LANGUAGE_INPUT_PROFILE)
        self.wait_until_text_present_element_value(self.LANGUAGE_INPUT, *self.LANGUAGE_INPUT_PROFILE)
        self.dropdown_select(*self.ROLE_INPUT_PROFILE).select_by_value(self.ROLE_INPUT)
        self.wait_until_text_present_element_value(self.ROLE_INPUT, *self.ROLE_INPUT_PROFILE)

    def check_test_info_input_fields(self):
        joined_input_value = self.find_elements(*self.JOINED_INPUT_PROFILE)[0].get_attribute('value')
        language_input_value = self.find_elements(*self.LANGUAGE_INPUT_PROFILE)[0].get_attribute('value')
        role_input_value = self.find_elements(*self.ROLE_INPUT_PROFILE)[0].get_attribute('value')
        print(f'"{joined_input_value}", "{language_input_value}", "{role_input_value}"')
        assert joined_input_value == self.JOINED_INPUT, f'Expected {self.JOINED_INPUT}, got {joined_input_value}'
        assert language_input_value == self.LANGUAGE_INPUT, f'Expected {self.LANGUAGE_INPUT}, got {language_input_value}'
        assert role_input_value == self.ROLE_INPUT, f'Expected {self.ROLE_INPUT}, got {role_input_value}'

    def check_close_save_buttons(self, browser_mode):
        if 'mobile' in browser_mode:
            self.wait_until_clickable(*self.PROFILE_BUTTON_SAVE)
            self.wait_until_clickable(*self.PROFILE_BUTTON_CLOSE)
        else:
            self.wait_until_clickable(*self.SAVE_BUTTON_PROFILE)
            self.wait_until_clickable(*self.CLOSE_BUTTON_PROFILE)
