from real_project_example.helper.pages.base_page import MAIN_URL
from real_project_example.helper.pages.composite_elements import LeftMenuElement


class CheckboxesPage(LeftMenuElement):

    url = MAIN_URL + '/checkbox'

    toggle_locator = '//span[@class="rct-text" and .="%s"]/button[@title="Toggle"]'
    checkbox_locator = '//span[@class="rct-title" and .="%s"]'

    def open_page(self):
        self.go_to(self.url)

    def get_checkbox_by_name(self, name):
        return self.find_by_xpath(self.checkbox_locator % name)

    def some(self):
        list_elements = self.find_elements_by_xpath('//span[@class="rct-title"]')
        for element in list_elements:
            element.click()
