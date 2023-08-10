from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


class Hrm_Login_Pg:
    username = "username"
    password = "password"
    login_btn = '//form/div[3]/button'
    dashboard_header_locator = "h6"
    invalid_credential_locator = '//p[text()="Invalid credentials"]'
    username_required_locator = "(//span[text()='Required'])[1]"
    password_required_locator = "(//span[text()='Required'])[2]"
    logout_dd = "//p[@class='oxd-userdropdown-name']"
    logout_txt = "//a[text()='Logout']"

    def __init__(self, a_driver):
        self.my_driver = a_driver

    def enter_username(self, p_username):
        self.my_driver.find_element(By.NAME, self.username).send_keys(p_username)

    def enter_password(self, p_password):
        self.my_driver.find_element(By.NAME, self.password).send_keys(p_password)

    def login(self):
        self.my_driver.find_element(By.XPATH, self.login_btn).click()

    def logout(self):
        self.my_driver.find_element(By.XPATH, self.logout_dd).click()
        self.my_driver.find_element(By.XPATH, self.logout_txt).click()

    def verify_successful_login(self):
        dashboard_header_text = self.my_driver.find_element(By.TAG_NAME, self.dashboard_header_locator).text
        assert dashboard_header_text == "Dashboard"

    def verify_unsuccessful_login_attempt(self):
        try:
            dashboard_header_text = self.my_driver.find_element(By.TAG_NAME, self.dashboard_header_locator).text
        except:
            pass
        invalid_credentials_text = self.my_driver.find_element(By.XPATH, self.invalid_credential_locator).text
        assert invalid_credentials_text == "Invalid credentials"

    def verify_unsuccessful_login_attempt_required_fields_missing(self):
        try:
            dashboard_header_text = self.my_driver.find_element(By.TAG_NAME, self.dashboard_header_locator).text
        except:
            pass
        username_required_text = self.my_driver.find_element(By.XPATH, self.username_required_locator).text
        assert username_required_text == "Required"
        password_required_text = self.my_driver.find_element(By.XPATH, self.password_required_locator).text
        assert password_required_text == "Required"
