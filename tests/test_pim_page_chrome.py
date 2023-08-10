import json
import os
import time
import unittest
from os.path import dirname as up
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from orangehrmpages.login_page_class import Hrm_Login_Pg
from orangehrmpages.pim_page_class import HRM_PIM_Page
from utilities.org_hrm_helper import org_hrm_logout
from utilities.util import check_for_title, take_screenshot


class PIMPgTestClass(unittest.TestCase):
    driver = None
    data_dict = None
    emp_id = 0


    @classmethod
    def setUpClass(cls) -> None:
        cwd = os.getcwd()
        cwd_one_up = up(up(__file__))
        json_file_path = cwd_one_up + "\\data_source\\org_hrm_test_data.json"
        with open(json_file_path) as json_file:
            cls.data_dict = json.load(json_file)
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        emp_id = 0

    def test_tc_pim_01_add_employee_successful(self):
        hrm_project = Hrm_Login_Pg(self.driver)
        hrm_project.enter_username(self.data_dict.get("login_credentials").get("correct_username"))
        hrm_project.enter_password(self.data_dict.get("login_credentials").get("correct_password"))
        hrm_project.login()
        check_for_title(self.driver, "Dashboard")

        hrm_pim_obj = HRM_PIM_Page(self.driver)
        hrm_pim_obj.navigate_to_pim_module()
        hrm_pim_obj.add_employee(self.data_dict.get("employee_info").get("f_name"),
                                 self.data_dict.get("employee_info").get("m_name"),
                                 self.data_dict.get("employee_info").get("l_name"))
        time.sleep(30)
        take_screenshot(self.driver, 'tc_pim_01_add_emp')
        self.emp_id = hrm_pim_obj.verify_successful_addition_of_employee(
            self.data_dict.get("employee_info").get("f_name"),
            self.data_dict.get("employee_info").get("l_name"))
        take_screenshot(self.driver, 'tc_pim_01_add_emp')
        hrm_pim_obj.employee_search_by_id(self.emp_id)
        take_screenshot(self.driver, 'tc_pim_02_edit_emp_by_id')

    def test_tc_pim_02_edit_employee_custom_personal_details_successful(self):
        hrm_pim_obj = HRM_PIM_Page(self.driver)
        hrm_pim_obj.navigate_to_pim_module()
        hrm_pim_obj.update_emp_personal_details_custom_fields(self.data_dict.get("employee_info").get("f_name"),
                                                              self.data_dict.get("employee_info").get("m_name"),
                                                              self.data_dict.get("employee_info").get("l_name"),
                                                              self.data_dict.get("employee_info").get("bg"))
        take_screenshot(self.driver, 'tc_pim_02_edit_emp')

    def test_tc_pim_03_edit_employee_standard_personal_details_successful(self):
        hrm_pim_obj = HRM_PIM_Page(self.driver)
        hrm_pim_obj.navigate_to_pim_module()
        hrm_pim_obj.update_emp_personal_details_std_fields(self.data_dict.get("employee_info").get("f_name"),
                                                           self.data_dict.get("employee_info").get("m_name"),
                                                           self.data_dict.get("employee_info").get("l_name"),
                                                           self.data_dict.get("employee_info").get("nickname"),
                                                           self.data_dict.get("employee_info").get("other_id"),
                                                           self.data_dict.get("employee_info").get("drivers_license"),
                                                           self.data_dict.get("employee_info").get("license_expiry_date"),
                                                           self.data_dict.get("employee_info").get("ssn"),
                                                           self.data_dict.get("employee_info").get("sin"),
                                                           self.data_dict.get("employee_info").get("nationality"),
                                                           self.data_dict.get("employee_info").get("marital_status"),
                                                           self.data_dict.get("employee_info").get("dob"),
                                                           self.data_dict.get("employee_info").get("gender"),
                                                           self.data_dict.get("employee_info").get("military"),
                                                           )
        take_screenshot(self.driver, 'tc_pim_03_edit_emp')

    def test_tc_pim_04_add_employee_prerequisite_for_deletion(self):
        hrm_pim_obj = HRM_PIM_Page(self.driver)
        hrm_pim_obj.navigate_to_pim_module()
        hrm_pim_obj.add_employee(self.data_dict.get("delete_employee_info").get("f_name"),
                                 self.data_dict.get("delete_employee_info").get("m_name"),
                                 self.data_dict.get("delete_employee_info").get("l_name"))
        time.sleep(30)
        take_screenshot(self.driver, 'tc_pim_04_prereq_add_emp')

    def test_tc_pim_04_delete_cancel(self):
        hrm_pim_obj = HRM_PIM_Page(self.driver)
        hrm_pim_obj.navigate_to_pim_module()
        hrm_pim_obj.pim_emp_search_and_select_for_deletion_cancel(
                                           self.data_dict.get("delete_employee_info").get("f_name"),
                                           self.data_dict.get("delete_employee_info").get("m_name"),
                                           self.data_dict.get("delete_employee_info").get("l_name"),)
        take_screenshot(self.driver, 'tc_pim_04_delete_cancel')

    def test_tc_pim_05_delete_success(self):
        hrm_pim_obj = HRM_PIM_Page(self.driver)
        hrm_pim_obj.navigate_to_pim_module()
        hrm_pim_obj.pim_emp_search_and_select_for_deletion(
                                           self.data_dict.get("delete_employee_info").get("f_name"),
                                           self.data_dict.get("delete_employee_info").get("m_name"),
                                           self.data_dict.get("delete_employee_info").get("l_name"),)
        take_screenshot(self.driver, 'tc_pim_05_delete_success')