from real_project_example.helper.pages.base_page import MAIN_URL
from real_project_example.helper.pages.composite_elements import LeftMenuElement


class WebTablesPage(LeftMenuElement):

    url = MAIN_URL + '/buttons'
    double_click_button = '//button[@id="doubleClickBtn"]'
    right_click_button = '//button[@id="rightClickBtn"]'
    click_me_button = '//button[.="Click Me"]'

    double_click_message = '//*[@id="doubleClickMessage"]'
    right_click_message = '//*[@id="rightClickMessage"]'
    dynamic_click_message = '//*[@id="dynamicClickMessage"]'

    def open_page(self):
        self.go_to(self.url)
