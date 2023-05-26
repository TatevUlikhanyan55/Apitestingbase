from selenium.webdriver.common.by import By
from DevilWearsPrada.lib import helpers


accept_cookies = (By.XPATH, '//*[@class="banner_cta cta_accept"]')
menu_navigation = (By.XPATH, "//*[@aria-label='Prada Navigation']")
women_section = (By.XPATH, "//*[@href='https://www.prada.com/ww/en/women.html']")
men_section = (By.XPATH, "//*[@href='https://www.prada.com/ww/en/men.html']")

def accept_cookies_btn_click():
    helpers.find_and_click(accept_cookies)



