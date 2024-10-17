from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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

    def wait_until_body_change(self, value):
        """ Wait until the <body> element's class attribute changes to the target body's class attribute name. """
        self.driver.wait.until(lambda driver: self.driver.find_element(By.TAG_NAME, 'body').get_attribute('class') == value)

    def move_to_element_and_click(self, *locator):
        """ Use ActionChains to move to an element and click on it."""
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def scroll_to_element_and_click(self, *locator):
        """ Scroll the element into view and then click it. """
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def scroll_to_bottom_and_verify(self, context):
        """ Scroll to the bottom of the page."""
        # Scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Get the total height of the page and the current scroll position
        total_page_height = self.driver.execute_script("return document.body.scrollHeight;")
        current_scroll_position = self.driver.execute_script("return window.pageYOffset + window.innerHeight;")

        # Verify scroll position
        if current_scroll_position >= total_page_height:
            context.logger.info('Successfully scrolled to the bottom')
        else:
            message = f'Expected to be at the bottom of page, but was not. Current scroll position: {current_scroll_position} out of {total_page_height}'
            context.logger.error(message)
            assert False, message
