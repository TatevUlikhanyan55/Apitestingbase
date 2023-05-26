from DevilWearsPrada.pages.Shoes_page import ShoesPage
from DevilWearsPrada.pages import Home_page
from DevilWearsPrada.lib import helpers
from DevilWearsPrada.testdata import test_data


def test_check_shoes_total_for_men():
    helpers.go_to_page(test_data.prada_shoes_page_url)
    # driver = helpers.driver
    Home_page.accept_cookies_btn_click()
    shoes_page = ShoesPage(helpers.driver)
    shoes_page.find_shoes_count_and_click_on_first_item()


if __name__ == '__main__':
    test_check_shoes_total_for_men()
