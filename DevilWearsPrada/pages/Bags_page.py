from selenium.webdriver.common.by import By
from DevilWearsPrada.lib import helpers
from DevilWearsPrada.pages import Home_page
from DevilWearsPrada.lib.log_info import logger
from DevilWearsPrada.lib.requests.get_requests import make_get_request
from DevilWearsPrada.lib import  endpoints


women_shoulder_bags = (By.XPATH, "//*[@href='https://www.prada.com/ww/en/women/bags/shoulder_bags.html']")
searched_product_count = (By.XPATH, "//*[@class='filter-alt__box--results-number']")


# def navigate_to_women_shoulder_bags_and_check_total():
#     Home_page.accept_cookies_btn_click()
#     total_shoulder_bags = helpers.find(searched_product_count, get_text=True)
#     logger(f'Finded shoulder bags amount is - {total_shoulder_bags}')

def navigate_to_women_shoulder_bags_and_check_total_via_api():
    response_dict = make_get_request(endpoints.view_all_women_bags)
    print(response_dict[0]['entry'][0]['count'])
    # total_shoulder_bags = response_dict["count"]
    # logger(f'Finded shoulder bags amount is - {total_shoulder_bags}')





