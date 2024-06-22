from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from real_project_example.helper.pages.base_page import MAIN_URL, BasePage
from real_project_example.helper.pages.composite_elements import LeftMenuElement


class WebTablesPage(LeftMenuElement):

    url = MAIN_URL + '/webtables'
    add_button = '//*[@id="addNewRecordButton"]'
    search_box_input = '//*[@id="searchBox"]'
    edit_record_button = '//*[@title="Edit"]'
    delete_record_button = '//*[@title="Delete"]'

    row_locator = '//*[@class="rt-tbody"]//div/div[@role="row"]/div[%s][.="%s"]/..'

    def open_page(self):
        self.go_to(self.url)

    @staticmethod
    def get_add_record_popup():
        return RegistrationFormPopup()

    def get_row_by_value(self, column_index, column_value):
        our_locator = self.row_locator % (column_index, column_value)
        return self.find_by_xpath(our_locator)

    def cell_by_name(self, row_element, column_index):
        return row_element.find_element(By.XPATH, f'./div[{column_index}]')


class RegistrationFormPopup(BasePage):
    modal_header = '//*[@id="registration-form-modal"]'
    first_name_input = '//*[@id="firstName"]'
    last_name_input = '//*[@id="lastName"]'
    email_input = '//*[@id="userEmail"]'
    age_input = '//*[@id="age"]'
    salary_input = '//*[@id="salary"]'
    department_input = '//*[@id="department"]'

    submit_button = '//*[@id="submit"]'
    close_button = '//button[@class="close"]'

    cell_locator = '//*[@class="rt-tbody"]//div[@role="gridcell" and .="%s"]'

    def get_cell_by_value(self, cell_value):
        try:
            cell_element = self.find_by_xpath(self.cell_locator % cell_value)
            return cell_element
        except NoSuchElementException:
            return False
