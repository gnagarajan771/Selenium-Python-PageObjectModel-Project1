import json
import os
import time
import unittest
from os.path import dirname as up

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from orangehrmpages.login_page_class import Hrm_Login_Pg
from utilities.org_hrm_helper import org_hrm_logout
from utilities.util import check_for_title, take_screenshot


class LoginPgTestClass(unittest.TestCase):
    driver = None
    data_dict = None

    @classmethod
    def setUpClass(cls) -> None:
        cwd = os.getcwd()
        cwd_one_up = up(up(__file__))
        json_file_path = cwd_one_up + "\\data_source\\org_hrm_test_data.json"
        with open(json_file_path) as json_file:
            cls.data_dict = json.load(json_file)
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(15)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def test_tc_login_01_success(self):
        print(self.data_dict.get("login_credentials").get("correct_username"))
        hrm_project = Hrm_Login_Pg(self.driver)
        hrm_project.enter_username(self.data_dict.get("login_credentials").get("correct_username"))
        hrm_project.enter_password(self.data_dict.get("login_credentials").get("correct_password"))
        hrm_project.login()
        check_for_title(self.driver, "Dashboard")
        take_screenshot(self.driver, 'tc_login_01_login_success')
        org_hrm_logout(self.driver)

    def test_tc_login_02_unsuccessful_blank_username_password(self):
        hrm_project = Hrm_Login_Pg(self.driver)
        hrm_project.enter_username(self.data_dict.get("login_credentials").get("blank_username"))
        hrm_project.enter_password(self.data_dict.get("login_credentials").get("blank_password"))
        hrm_project.login()
        hrm_project.verify_unsuccessful_login_attempt_required_fields_missing()
        take_screenshot(self.driver, 'tc_login_02_unsuccessful_blanks')


    def test_tc_login_03_unsuccessful_incorrect_username(self):
        hrm_project = Hrm_Login_Pg(self.driver)
        hrm_project.enter_username(self.data_dict.get("login_credentials").get("incorrect_username"))
        hrm_project.enter_password("admin123")
        hrm_project.login()
        hrm_project.verify_unsuccessful_login_attempt()
        take_screenshot(self.driver, 'tc_login_03_unsuccessful_username_issue')

    def test_tc_login_04_unsuccessful_incorrect_password(self):
        hrm_project = Hrm_Login_Pg(self.driver)
        hrm_project.enter_username(self.data_dict.get("login_credentials").get("correct_username"))
        hrm_project.enter_password(self.data_dict.get("login_credentials").get("incorrect_password"))
        hrm_project.login()
        hrm_project.verify_unsuccessful_login_attempt()
        take_screenshot(self.driver, 'tc_login_04_unsuccessful_pwd_issue')



