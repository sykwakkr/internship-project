from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep


class PageBase:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def is_field_filed_by_w_input(self, *locator):
        return self.driver.find_element(*locator).get_attribute('value') != 'undefined'

    def is_field_filed_done(self, value, *locator):
        return self.driver.find_element(*locator).get_attribute('value') == value

    def clear_input(self, *locator):
        self.driver.find_element(*locator).clear()

    def input_text(self, text, *locator):
        # self.driver.wait.until(lambda driver: self.is_field_filed_by_w_input(*locator))
        self.clear_input(*locator)
        self.driver.find_element(*locator).send_keys(text)
        # self.driver.wait.until(lambda driver: self.is_field_filed_done(text, *locator))

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def dropdown_select(self, *locator):
        select = Select(self.find_elements(*locator)[0])
        return select

    def wait_until_all_visible(self, *locator):
        self.driver.wait.until(EC.visibility_of_all_elements_located(locator), message=f'All Elements are not visible.')

    def wait_until_clickable(self, *locator):
        self.driver.wait.until(EC.element_to_be_clickable(locator), message=f'Clickable Elements are not visible.')

    def wait_until_title_is(self, title):
        self.driver.wait.until(EC.title_is(title), message=f'Title "{title}" is not available.')

    def wait_until_url_is(self, url):
        self.driver.wait.until(EC.url_to_be(url), message=f'URL "{url}" is not available.')