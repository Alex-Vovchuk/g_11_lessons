import random

from faker import Faker
from selenium.webdriver.common.by import By

from real_project_example.helper.pages.web_tables_page import WebTablesPage


class TestWebTablesAddRecord:

    def test_add_new_record(self):
        faker = Faker()
        first_name = faker.first_name()
        last_name = faker.last_name()
        age = random.randint(10, 99)
        email = faker.email()
        salary = random.randint(1000, 9900)
        department = faker.word()
        tables_page = WebTablesPage()
        tables_page.open_page()

        tables_page.wait_for_clickable(tables_page.add_button).find_by_xpath(tables_page.add_button).click()

        registration_form = tables_page.get_add_record_popup()
        registration_form.find_by_xpath(registration_form.first_name_input).send_keys(first_name)
        registration_form.find_by_xpath(registration_form.last_name_input).send_keys(last_name)
        registration_form.find_by_xpath(registration_form.email_input).send_keys(email)
        registration_form.find_by_xpath(registration_form.age_input).send_keys(age)
        registration_form.find_by_xpath(registration_form.salary_input).send_keys(salary)
        registration_form.find_by_xpath(registration_form.department_input).send_keys(department)

        registration_form.find_by_xpath(registration_form.submit_button).click()
        registration_form.wait_for_element_invisible(registration_form.modal_header)

        assert registration_form.get_cell_by_value(first_name)

        record_row = tables_page.get_row_by_value(column_names['First Name'], first_name)

        assert record_row.find_element(By.XPATH, './div[1]').text == first_name
        assert record_row.find_element(By.XPATH, './div[2]').text == last_name
        assert record_row.find_element(By.XPATH, './div[3]').text == str(age)
        assert record_row.find_element(By.XPATH, './div[4]').text == email


column_names = {'First Name': 1, 'Last Name': 2, 'Age': 3, 'Email': 4}



# class TestWebTablesSearchRecord:
# class TestWebTablesEditRecord: