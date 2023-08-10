import subprocess
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

from utilities.util import check_for_title, take_screenshot


class HRM_PIM_Page:
    element_pim_link = "//span[text()='PIM']"
    add_employee_btn = "//button[text()=' Add ']"
    emp_first_name = "firstName"
    emp_middle_name = "middleName"
    emp_last_name = "lastName"
    save_btn = "//button[text()=' Save ']"
    emp_id = 0
    emp_list = []
    pim_pg_tabs = "//a[@class='oxd-topbar-body-nav-tab-item']"
    pim_emp_total = "//div[@class='orangehrm-header-container']/following-sibling::div/div[1]/span"
    pim_emp_search_by_name = "//input[@placeholder='Type for hints...'][1]"
    pim_emp_search_btn = "//button[@type='submit']"
    pim_search_no_records_found = "//span[text()='No Records Found']"
    pim_delete_emp_btn = "//button[text()=' Delete Selected ']"
    pim_emp_yes_delete = "//button[text()=' Yes, Delete ']"
    pim_emp_no_cancel = "//button[text()=' No, Cancel ']"
    pim_search_results_table = "//*[@role='table']/div[2]/div"
    pim_search_results_table_select_ck_box = "(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon'])[2]"
    pim_search_results_table_emp_id = "//div[@class='oxd-table-body']/div/div/div[2]/div"
    pim_search_results_table_emp_first_and_middle_name = "//div[@class='oxd-table-body']/div/div/div[3]/div"
    pim_emp_fname_search_input = "//input[@placeholder='Type for hints...'][1]"
    pim_emp_search_id_label = "//label[text()='Employee Id']"
    pim_search_table_rows = "//div[@class='oxd-table-card']"
    pim_add_img_btn = "//div[@class='employee-image-wrapper']//following-sibling::button"
    pim_details_emp_nickname = "//label[text()='Nickname']"
    pim_details_emp_other_id = "//label[text()='Other Id']"
    pim_emp_id_label = "//label[text()='Employee Id']"
    pim_emp_drivers_license_label = "//label[contains (text(), 'License Number')]"
    pim_emp_drivers_license_expiry_label = "//label[text()='License Expiry Date']"
    pim_emp_ssn_label = "//label[text()='SSN Number']"
    pim_emp_sin_label = "//label[text()='SIN Number']"
    pim_emp_nationality_label = "//label[text()='Nationality']"
    pim_emp_nationality_dd = "(//div[@class='oxd-select-text-input'])[1]"
    pim_emp_marital_status_label = "//label[text()='Marital Status']"
    pim_emp_marital_status_dd = "(//div[@class='oxd-select-text-input'])[2]"
    pim_emp_dob_label = "//label[text()='Date of Birth']"
    pim_emp_gender_male = "//input[@type='radio'][@value='1']"
    pim_emp_gender_female = "//input[@type='radio'][@value='2']"
    pim_emp_military_status = "//label[text()='Military Service']"
    pim_emp_smokes_checkbox = "//input[@type='checkbox']//following-sibling::span"
    pim_emp_blood_group_dd = "(//div[@class='oxd-select-text-input'])[3]"
    pim_emp_standard_fields_save_btn = "(//form[@class='oxd-form']//button[text()=' Save '])[1]"
    pim_emp_custom_field_save_btn = "//div[@class='orangehrm-custom-fields']//button[text()=' Save ']"
    pim_emp_id_exists_msg = "//span[text()='Employee Id already exists']"

    def __init__(self, a_driver):
        self.my_driver = a_driver
        self.my_driver.implicitly_wait(5)

    def auto_it_upload(self):
        script_path = "C:\\C Drive_GUVI_Lectures\\auto_id_exe\\Orange.exe"
        subprocess.run(script_path, shell=True)

    def navigate_to_pim_module(self):
        self.my_driver.find_element(By.XPATH, self.element_pim_link).click()
        check_for_title(self.my_driver, "PIM")

    def add_employee(self, f_name, m_name, l_name):
        self.my_driver.find_element(By.XPATH, self.add_employee_btn).click()
        self.my_driver.find_element(By.NAME, self.emp_first_name).send_keys(f_name)
        self.my_driver.find_element(By.NAME, self.emp_middle_name).send_keys(m_name)
        self.my_driver.find_element(By.NAME, self.emp_last_name).send_keys(l_name)
        # self.my_driver.find_element(By.XPATH, self.pim_add_img_btn).click()
        # time.sleep(5)
        # self.auto_it_upload()
        time.sleep(5)
        self.my_driver.find_element(By.XPATH, self.save_btn).click()
        try:
            self.my_driver.find_element(By.XPATH, "//span[text()='Employee Id already exists']")
            print("Error during the updation process: Employee Id already exists")
        except:
            pass


    def update_emp_personal_details_custom_fields(self, f_name, m_name, l_name, blood_grp):
        self.employee_search_by_name(f_name, m_name, l_name)
        self.my_driver.execute_script(
            f"document.getElementsByClassName('oxd-select-text-input')[2].textContent='{blood_grp}'")
        blood_group_val = self.my_driver.execute_script(
            "return document.getElementsByClassName('oxd-select-text-input')[2].textContent")
        print(blood_group_val)
        self.my_driver.find_element(By.XPATH, self.pim_emp_custom_field_save_btn).click()
        assert blood_group_val == blood_grp
        time.sleep(10)

    def update_emp_personal_details_std_fields(self, *args):
        self.employee_search_by_name(args[0], args[1], args[2])
        nickname_label = self.my_driver.find_element(By.XPATH, self.pim_details_emp_nickname)
        self.my_driver.find_element(locate_with(By.TAG_NAME, "input").below(nickname_label)).send_keys(args[3])
        other_id_label = self.my_driver.find_element(By.XPATH, self.pim_details_emp_other_id)
        self.my_driver.find_element(locate_with(By.TAG_NAME, "input").below(other_id_label)).send_keys(args[4])
        driver_license_label = self.my_driver.find_element(By.XPATH, self.pim_emp_drivers_license_label)
        self.my_driver.find_element(locate_with(By.TAG_NAME, "input").below(driver_license_label)).send_keys(args[5])
        driver_license_expiry_label = self.my_driver.find_element(By.XPATH, self.pim_emp_drivers_license_expiry_label)
        self.my_driver.find_element(locate_with(By.TAG_NAME, "input").below(driver_license_expiry_label)).send_keys(args[6])
        ssn_label = self.my_driver.find_element(By.XPATH, self.pim_emp_ssn_label)
        self.my_driver.find_element(locate_with(By.TAG_NAME, "input").below(ssn_label)).send_keys(args[7])
        sin_label = self.my_driver.find_element(By.XPATH, self.pim_emp_sin_label)
        self.my_driver.find_element(locate_with(By.TAG_NAME, "input").below(sin_label)).send_keys(args[8])
        marital_status_label = self.my_driver.find_element(By.XPATH, self.pim_emp_marital_status_label)
        self.my_driver.execute_script(f"document.getElementsByClassName('oxd-select-text-input')[1].textContent = '{args[10]}'")
        dob_label = self.my_driver.find_element(By.XPATH, self.pim_emp_dob_label)
        self.my_driver.find_element(locate_with(By.TAG_NAME, "input").below(dob_label)).send_keys(args[11])
        gender_male = self.my_driver.find_element(By.XPATH, self.pim_emp_gender_male)
        self.my_driver.execute_script("arguments[0].click;", gender_male)
        military_label = self.my_driver.find_element(By.XPATH, self.pim_emp_military_status)
        self.my_driver.find_element(locate_with(By.TAG_NAME, "input").below(military_label)).send_keys(args[13])
        self.my_driver.execute_script(f"document.getElementsByClassName('oxd-select-text-input')[0].textContent='{args[9]}'")
        smoker_label = self.my_driver.find_element(By.XPATH, self.pim_emp_smokes_checkbox).click()

        self.my_driver.find_element(By.XPATH, self.pim_emp_standard_fields_save_btn).click()
        time.sleep(10)

        try:
            self.my_driver.find_element(By.XPATH, self.pim_emp_id_exists_msg)
            emp_id_label = self.my_driver.find_element(By.XPATH, self.pim_emp_id_label)
            self.emp_id = self.my_driver.execute_script(
                'return document.getElementsByClassName("oxd-input oxd-input--active")[5].value')
            print("Employee ID already exists", self.emp_id)
        except:
            pass

        emp_id_label = self.my_driver.find_element(By.XPATH, self.pim_emp_id_label)
        actions = ActionChains(self.my_driver)
        actions.move_to_element(emp_id_label).perform()
        take_screenshot(self.my_driver)
        self.navigate_to_pim_module()
        self.employee_search_by_name(args[0], args[1], args[2])
        updated_nickname = self.my_driver.execute_script(
            "return document.getElementsByClassName('oxd-input oxd-input--active')[4].value")
        print(args[3])
        assert updated_nickname == args[3]
        updated_other_id = self.my_driver.execute_script(
            "return document.getElementsByClassName('oxd-input oxd-input--active')[6].value")
        print(args[4])
        assert updated_other_id == args[4]
        updated_drivers_license = self.my_driver.execute_script(
            "return document.getElementsByClassName('oxd-input oxd-input--active')[7].value")
        print(args[5])
        assert updated_drivers_license == args[5]
        updated_drivers_license_expiry = self.my_driver.execute_script(
            "return document.getElementsByClassName('oxd-input oxd-input--active')[8].value")
        print(args[6])
        assert updated_drivers_license_expiry == args[6]
        updated_ssn = self.my_driver.execute_script(
            "return document.getElementsByClassName('oxd-input oxd-input--active')[9].value")
        print(args[7])
        assert updated_ssn == args[7]
        updated_sim = self.my_driver.execute_script(
            "return document.getElementsByClassName('oxd-input oxd-input--active')[10].value")
        print(args[8])
        assert updated_sim == args[8]
        updated_dob = self.my_driver.execute_script(
            "return document.getElementsByClassName('oxd-input oxd-input--active')[11].value")
        print(args[11])
        assert updated_dob == args[11]
        updated_military_status = self.my_driver.execute_script(
            "return document.getElementsByClassName('oxd-input oxd-input--active')[12].value")
        print(args[13])
        assert updated_military_status == args[13]

    def verify_successful_addition_of_employee(self, f_name, l_name):
        name_check = f_name + ' ' + l_name
        assert self.my_driver.find_element(By.XPATH, f"//h6[text()='{name_check}']")
        assert self.my_driver.find_element(By.XPATH, self.pim_emp_id_label)
        time.sleep(5)
        emp_id_label = self.my_driver.find_element(By.XPATH, self.pim_emp_id_label)
        self.emp_id = self.my_driver.execute_script(
            'return document.getElementsByClassName("oxd-input oxd-input--active")[5].value')
        self.employee_search(self.emp_id)
        return (self.emp_id)

    def employee_search(self, emp_id):
        pim_search_results_grid = self.my_driver.find_elements(By.XPATH, self.pim_search_results_table)
        element_add_employee = self.my_driver.find_elements(By.XPATH, self.pim_pg_tabs)
        element_add_employee[0].click()
        time.sleep(5)
        pim_employee_list_search = self.my_driver.find_element(By.XPATH, self.pim_emp_fname_search_input)
        pim_search_employee = self.my_driver.find_element(By.XPATH, "//button[@type='submit']")
        pim_search_employee.click()
        time.sleep(5)
        try:
            pim_search_results_grid_emp_id = self.my_driver.find_element(By.XPATH, self.pim_search_results_table_emp_id)
            total_number_of_records_span_text = self.my_driver.find_element(By.XPATH, self.pim_emp_total)
            print(total_number_of_records_span_text.text)
            pim_search_results_grid_1_of_x_pages = self.my_driver.find_elements(By.XPATH, self.pim_search_table_rows)
            try:
                for i in range(1, len(pim_search_results_grid_1_of_x_pages) + 1):
                    self.emp_list.append(self.my_driver.find_element(By.XPATH,
                                                                     f'//div[@class="oxd-table-card"][{i}]/div/div[2]/div').text)
            except Exception as e:
                print(e)

            for emp_results_pg_number in range(2, 100):
                try:
                    self.my_driver.find_element(By.XPATH, f"//ul[@class='oxd-pagination__ul']/li[2]/button[text()={emp_results_pg_number}]").click()
                    total_number_of_records_span_text = self.my_driver.find_element(By.XPATH, self.pim_emp_total)
                    print(total_number_of_records_span_text.text)
                    pim_search_results_grid_1_of_x_pages = self.my_driver.find_elements(By.XPATH, self.pim_search_table_rows)

                    for i in range(1, len(pim_search_results_grid_1_of_x_pages) + 1):
                        self.emp_list.append(self.my_driver.find_element(By.XPATH, f'//div[@class="oxd-table-card"][{i}]/div/div[2]/div').text)
                    take_screenshot(self.my_driver)
                except Exception as e:
                    break
        except Exception as e:
            print("No records found", e)
        assert self.emp_id in self.emp_list

    def employee_search_by_id(self, emp_id):
        pim_emp_search_id_label_element = self.my_driver.find_element(By.XPATH, self.pim_emp_search_id_label)
        emp_id_input = self.my_driver.find_element(
            locate_with(By.TAG_NAME, "input").below(pim_emp_search_id_label_element))
        emp_id_input.send_keys(emp_id)
        pim_search_employee = self.my_driver.find_element(By.XPATH, self.pim_emp_search_btn)
        pim_search_employee.click()
        time.sleep(5)
        try:
            pim_search_results_grid_emp_id = self.my_driver.find_element(By.XPATH, self.pim_search_results_table_emp_id)
            emp_id_element = self.my_driver.find_element(By.XPATH, f'//div[text()="{emp_id}"]')
            emp_id_element.click()
            time.sleep(5)
        except Exception as e:
            print(e)

    def employee_search_by_name(self, f_name, m_name, l_name):
        pim_employee_list_search = self.my_driver.find_element(By.XPATH, self.pim_emp_search_by_name)
        pim_employee_list_search.send_keys(f_name + " " + m_name + " " + l_name)
        time.sleep(5)
        pim_search_employee = self.my_driver.find_element(By.XPATH, self.pim_emp_search_btn)
        pim_search_employee.click()
        time.sleep(10)
        first_plus_middle_name = f_name + " " + m_name
        try:
            pim_search_results_grid_name = self.my_driver.find_element(By.XPATH, self.pim_search_results_table_emp_first_and_middle_name)
            emp_name_element = self.my_driver.find_element(By.XPATH, f'//div[text()="{first_plus_middle_name}"]')
            emp_name_element.click()
            time.sleep(5)
        except Exception as e:
            print("exception in employee search method", e)

    def pim_emp_search_and_select_for_deletion_cancel(self, f_name, m_name, l_name):
        pim_employee_list_search = self.my_driver.find_element(By.XPATH, self.pim_emp_search_by_name)
        pim_employee_list_search.send_keys(f_name + " " + m_name + " " + l_name)
        pim_search_employee = self.my_driver.find_element(By.XPATH, self.pim_emp_search_btn)
        pim_search_employee.click()
        time.sleep(5)
        first_plus_middle_name = f_name + " " + m_name

        pim_search_results_grid_name_ck = self.my_driver.find_element(By.XPATH, self.pim_search_results_table_select_ck_box)
        pim_search_results_grid_name_ck.click()
        time.sleep(2)
        self.my_driver.find_element(By.XPATH, self.pim_delete_emp_btn).click()
        take_screenshot(self.my_driver)
        self.my_driver.find_element(By.XPATH, self.pim_emp_no_cancel).click()
        take_screenshot(self.my_driver)
        pim_search_employee.click()
        time.sleep(5)
        pim_search_results_grid_name = self.my_driver.find_element(By.XPATH, self.pim_search_results_table_emp_first_and_middle_name)
        emp_name_element = self.my_driver.find_element(By.XPATH, f'//div[text()="{first_plus_middle_name}"]')

    def pim_emp_search_and_select_for_deletion(self, f_name, m_name, l_name):
        pim_employee_list_search = self.my_driver.find_element(By.XPATH, self.pim_emp_search_by_name)
        pim_employee_list_search.send_keys(f_name + " " + m_name + " " + l_name)
        pim_search_employee = self.my_driver.find_element(By.XPATH, self.pim_emp_search_btn)
        pim_search_employee.click()
        time.sleep(5)
        first_plus_middle_name = f_name + " " + m_name
        try:
            pim_search_results_grid_name_ck = self.my_driver.find_element(By.XPATH, self.pim_search_results_table_select_ck_box)
            emp_id_to_delete = self.my_driver.find_element(By.XPATH, '//div[@class="oxd-table-card"][1]/div/div[2]/div').text
            pim_search_results_grid_name_ck.click()
            time.sleep(2)
            self.my_driver.find_element(By.XPATH, self.pim_delete_emp_btn).click()
            take_screenshot(self.my_driver)
            self.my_driver.find_element(By.XPATH, self.pim_emp_yes_delete).click()
            take_screenshot(self.my_driver)
        except Exception as e:
            print (e)

        pim_emp_search_id_label_element = self.my_driver.find_element(By.XPATH, self.pim_emp_search_id_label)
        emp_id_input = self.my_driver.find_element(
            locate_with(By.TAG_NAME, "input").below(pim_emp_search_id_label_element))
        emp_id_input.send_keys(emp_id_to_delete)
        pim_search_employee.click()
        time.sleep(5)
        pim_search_results_no_records = self.my_driver.find_element(By.XPATH, self.pim_search_no_records_found).text
        assert pim_search_results_no_records == "No Records Found"
