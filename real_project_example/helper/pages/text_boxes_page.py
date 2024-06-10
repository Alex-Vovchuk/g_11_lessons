
from real_project_example.helper.pages.base_page import MAIN_URL
from real_project_example.helper.pages.composite_elements import LeftMenuElement


class TextBoxesPage(LeftMenuElement):

    url = MAIN_URL + '/text-box'
    name_input = '//input[@id="userName"]'
    email_input = '//*[@id="userEmail"]'
    current_address_input = '//textarea[@id="currentAddress"]'
    permanent_address_input = '//textarea[@id="permanentAddress"]'

    submit_button = '//*[@id="submit"]'

    name_message = '//p[@id="name"]'
    email_message = '//p[@id="email"]'
    current_address_message = '//p[@id="currentAddress"]'
    permanent_address_message = '//p[@id="permanentAddress"]'

    def open_page(self):
        self.go_to(self.url)
