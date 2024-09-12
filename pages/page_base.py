from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep


class PageBase:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def clear_input(self, *locator):
        self.driver.find_element(*locator).clear()

    def input_text(self, text, *locator):
        self.clear_input(*locator)
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def dropdown_select(self, *locator):
        select = Select(self.find_elements(*locator)[0])
        return select

    def wait_until_all_visible_located(self, *locator):
        self.driver.wait.until(EC.visibility_of_all_elements_located(locator), message=f'All Elements are not visible.')

    def wait_until_clickable(self, *locator):
        self.driver.wait.until(EC.element_to_be_clickable(locator), message=f'Clickable Elements are not visible.')

    def wait_until_url_contains(self, url):
        self.driver.wait.until(EC.url_contains(url))

    def wait_until_not_text_present_element(self, text, *locator):
        self.driver.wait.until_not(EC.text_to_be_present_in_element(locator, text))

    def wait_until_not_text_present_element_value(self, value, *locator):
        self.driver.wait.until_not(EC.text_to_be_present_in_element_value(locator, value))

    def wait_until_text_present_element_value(self, value, *locator):
        self.driver.wait.until(EC.text_to_be_present_in_element_value(locator, value))

    def clear_text(self, *locator):
        self.driver.find_element(*locator).clear()
