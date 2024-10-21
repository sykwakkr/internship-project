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
    LISTING_TYPE_BUY = (By.XPATH, '//div[contains(text(), "Want to buy")]')
    LISTING_TYPE_ALL = (By.XPATH, '//div[contains(text(), "All")]')
    SWITCHER_BUTTON_ACTIVE = (By.CSS_SELECTOR, 'div.switcher-button.active')
    APPLY_FILTER_BUTTON = (By.CSS_SELECTOR, 'a.button-filter.w-button')
    SALE_TAG_MLS_BUY = (By.XPATH, '//div[@wized="saleTagMLS" and text()="Want to buy"]')
    SALE_TAG_MLS_SELL = (By.XPATH, '//div[@wized="saleTagMLS" and text()="for sale"]')
    SALE_TAG_MLS = (By.XPATH, '//div[@wized="saleTagMLS"]')
    NEXT_PAGE_MLS = (By.CSS_SELECTOR, 'a[wized="nextPageMLS"]')

    def verify_right_page_opens(self):
        self.wait_until_all_visible_located(*self.LISTING_CARD_MLS)
        current_page_count = int(self.find_elements(*self.CURRENT_PAGE_COUNT)[0].text)
        total_page_count = int(self.find_elements(*self.TOTAL_PAGE_COUNT)[0].text)
        print(f'Current Page Count: {current_page_count}, Total Page Count: {total_page_count}')
        assert current_page_count > 0 and total_page_count > 0, f'Page Count: {current_page_count} / {total_page_count}'

    def click_filters(self):
        self.click_element(*self.FILTER_BUTTON)

    def click_filters_listing_type(self, listing_type='All'):
        """Filter by 'Want to sell' or 'Want to buy'. The default is 'All'.

        :param listing_type: string - 'Want to sell' or 'Want to buy' from test_secondary_page.feature
        :return: None
        """

        # Click 'Want to sell' or 'Want to buy' from the filter. To test "Fail', comment out the move_to_and_click()
        self.wait_until_all_visible_located(*self.SWITCHER_BUTTON_ACTIVE)
        if listing_type == 'Want to sell':
            self.move_to_element_and_click(*self.LISTING_TYPE_SELL)
        elif listing_type == 'Want to buy':
            self.move_to_element_and_click(*self.LISTING_TYPE_BUY)
        else:
            self.wait_until_all_visible_located(*self.LISTING_TYPE_ALL)

    def click_filters_apply(self):
        # Click 'Apply' button to filter by sell or buy.
        self.click_element(*self.APPLY_FILTER_BUTTON)

    def verify_all_cards_have_correct_tag(self, context, sale_tag, total_page_count=4):
        """ Verify that all card have correct tag on all pages by clicking on the next page button

            :param context: class - an instance of the logger class
            :param sale_tag: string - 'for sale' or 'Want to buy' from test_secondary_page.feature
            :param total_page_count: int - number of pages to check for testing purpose
            :return: None
        """

        self.wait_until_all_visible_located(*self.SALE_TAG_MLS)
        current_page_count = 1
        total_page_count = int(self.find_elements(*self.TOTAL_PAGE_COUNT)[0].text)  # Comment out for 4 pages testing.

        # Check all the pages with the next page button.
        while current_page_count <= total_page_count:
            if sale_tag == 'for sale':
                count_buy = len(self.find_elements(*self.SALE_TAG_MLS_BUY))
                assert count_buy == 0, f'Expected For Sale Only but {count_buy} "Want to buy" exist.'
            elif sale_tag == 'Want to buy':
                count_sell = len(self.find_elements(*self.SALE_TAG_MLS_SELL))
                assert count_sell == 0, f'Expected For Sale Only but {count_sell} "Want to sell" exist.'
            else:
                count_all = len(self.find_elements(*self.SALE_TAG_MLS))
                assert count_all > 0, f'Listing Type Fileter is selected with "All". It should be more than 0.'
            print(f'Total Page Count: {total_page_count}, Current Page Count: {current_page_count}')

            #  Check if TAG are all visible at the page
            sale_tag_mls = len(self.find_elements(*self.SALE_TAG_MLS))
            print(f'Number of TAG: {sale_tag_mls}')

            # Scroll down and click the next page button until the last page
            if current_page_count != total_page_count:
                self.scroll_to_bottom_and_verify(context)
                self.scroll_to_element_and_click(*self.NEXT_PAGE_MLS)
                try:
                    self.wait_until_all_visible_located(*self.SALE_TAG_MLS)
                except TimeoutException:
                    print(f'The elements did not become visible within the timeout period at {current_page_count}')
                    sleep(4)
            current_page_count += 1

