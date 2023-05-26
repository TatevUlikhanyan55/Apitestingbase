# pip install selenium-page-factory
import time

from seleniumpagefactory.Pagefactory import PageFactory
from DevilWearsPrada.lib.log_info import logger


class ShoesPage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.timeout = 30
        self.highlight = True

    locators = {
        'loafers_filter': ('XPATH', "//a[contains(text(),'Loafers')]"),
        'sandals_filter': ('XPATH', "//a[contains(text(),'Sandals')]"),
        'first_item': ('XPATH', '(//*[@class="productQB__title"])[1]'),
        'finded_product_count': ('XPATH', "//*[@class='filter-alt__box--results-number']")

    }

    def find_shoes_count_and_click_on_first_item(self):
        shoes_count = self.finded_product_count.get_text()
        logger(f'Finded man shoes amount is - {shoes_count}')
        self.highlight_web_element(self.finded_product_count)
        time.sleep(10)
        self.first_item.click_button()

# https://selenium-page-factory.readthedocs.io/en/latest/
# note: Every WebElement will be created after verifying
# it’s Presence and visibility on Page at Run-Time.
