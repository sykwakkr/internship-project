from selenium.common import TimeoutException

from pages.page_base import PageBase
from selenium.webdriver.common.by import By
from time import sleep


class PageSecondary(PageBase):
    LISTING_CARD_MLS = (By.CSS_SELECTOR, 'div.listing-card[w-list-index-value="0"] img.img-agent-listing[src*="http"]')
    CURRENT_PAGE_COUNT = (By.CSS_SELECTOR, 'div[wized="currentPageProperties"]')
    TOTAL_PAGE_COUNT = (By.CSS_SELECTOR, 'div[wized="totalPageProperties"]')
    FILTER_BUTTON = (By.CSS_SELECTOR, 'div.filter-button')
    LISTING_TYPE_SELL = (By.XPATH, '//div[contains(text(), "Want to sell")]')
    SWITCHER_BUTTON_ACTIVE = (By.CSS_SELECTOR, 'div.switcher-button.active')
    APPLY_FILTER_BUTTON = (By.CSS_SELECTOR, 'a.button-filter.w-button')
    SALE_TAG_MLS_BUY = (By.XPATH, '//div[@wized="saleTagMLS" and text()="Want to buy"]')
    NEXT_PAGE_MLS = (By.CSS_SELECTOR, 'a[wized="nextPageMLS"]')

    def verify_right_page_opens(self):
        self.wait_until_all_visible_located(*self.LISTING_CARD_MLS)
        current_page_count = int(self.find_elements(*self.CURRENT_PAGE_COUNT)[0].text)
        total_page_count = int(self.find_elements(*self.TOTAL_PAGE_COUNT)[0].text)
        print(f'Current Page Count: {current_page_count}, Total Page Count: {total_page_count}')
        assert current_page_count > 0 and total_page_count > 0, f'Page Count: {current_page_count} / {total_page_count}'

    def click_filters(self):
        self.click_element(*self.FILTER_BUTTON)

    def click_filters_sell(self):
        self.wait_until_all_visible_located(*self.SWITCHER_BUTTON_ACTIVE)
        self.move_to_element_and_click(*self.LISTING_TYPE_SELL)  # To test "Fail", comment out this line

    def click_filters_apply(self):
        self.click_element(*self.APPLY_FILTER_BUTTON)
        self.wait_until_all_visible_located(*self.LISTING_CARD_MLS)

    def verify_all_cards_have_for_sale(self, context):
        self.wait_until_all_visible_located(*self.LISTING_CARD_MLS)
        current_page_count = 1
        total_page_count = int(self.find_elements(*self.TOTAL_PAGE_COUNT)[0].text)
        total_page_count = 3
        while current_page_count < total_page_count:
            count_buy = len(self.find_elements(*self.SALE_TAG_MLS_BUY))
            assert count_buy == 0, f'Expected For Sale Only but {count_buy} "Want to buy" exist.'
            print(f'Total Page Count: {total_page_count}, Current Page Count: {current_page_count}')
            current_page_count += 1
            if current_page_count < total_page_count:
                self.scroll_to_bottom_and_verify(context)
                self.scroll_to_element_and_click(*self.NEXT_PAGE_MLS)
                try:
                    self.wait_until_all_visible_located(*self.LISTING_CARD_MLS)
                except TimeoutException:
                    print(f'The elements did not become visible within the timeout period at {current_page_count - 1}')
                    sleep(4)


