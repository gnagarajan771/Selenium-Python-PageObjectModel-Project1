from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def org_hrm_logout(driver):
    driver.find_element(By.XPATH, '//p[@class="oxd-userdropdown-name"]').click()
    logout_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Logout']")))
    logout_btn.click()
