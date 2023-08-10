import os
import datetime

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from multipledispatch import dispatch


def check_for_title(driver, title_name):
    dashboard_header_locator = "h6"
    dashboard_header_locator = driver.find_element(By.TAG_NAME, dashboard_header_locator)
    if dashboard_header_locator is not None:
        return True


@dispatch(selenium.webdriver.chrome.webdriver.WebDriver)
def take_screenshot(my_driver):
    vDate = datetime.datetime.now().date()
    vHOUR = datetime.datetime.now().hour  # the current hour
    vMINUTE = datetime.datetime.now().minute  # the current minute
    vSECONDS = datetime.datetime.now().second  # the current second
    result = str(vDate) + "_ts" + str(vHOUR) + str(vMINUTE) + str(vSECONDS)
    cwd = os.getcwd()
    my_driver.get_screenshot_as_file(
        f"C:\\Users\\gayat\\PycharmProjects\\pythonProject\\AT_Project1_OrangeHRM\\org_hrm_screenshots\\{result}.png")


@dispatch(selenium.webdriver.chrome.webdriver.WebDriver, str)
def take_screenshot(my_driver, testcase_name):
    vDate = datetime.datetime.now().date()
    vHOUR = datetime.datetime.now().hour  # the current hour
    vMINUTE = datetime.datetime.now().minute  # the current minute
    vSECONDS = datetime.datetime.now().second  # the current second
    result = "__" + str(vDate) + "_ts" + str(vHOUR) + str(vMINUTE) + str(vSECONDS)
    cwd = os.getcwd()
    my_driver.get_screenshot_as_file(
        f"C:\\Users\\gayat\\PycharmProjects\\pythonProject\\AT_Project1_OrangeHRM\\org_hrm_screenshots\\{testcase_name}{result}.png")


def scroll_to_page(my_driver, element_selenium):
    my_driver.execute_script("arguments[0].scrollIntoView(true);", element_selenium)


def wait_for_element(my_driver, element_selenium):
    WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, element_selenium)))
