from selenium import webdriver


def get_driver_by_name(driver_name):
    if driver_name == "chrome":
        return webdriver.Chrome()
    elif driver_name == "edge":
        return webdriver.ChromiumEdge()
    elif driver_name == "firefox":
        return webdriver.Firefox()
    else:
        print("Driver name is missing")
