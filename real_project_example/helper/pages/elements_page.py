from test_framework_example.browser import Browser
from test_framework_example.constants import MAIN_URL
from test_framework_example.helpers.pages.base_page import BasePage
from test_framework_example.helpers.pages.composite_elements import LeftMenuCompositeElement
from test_framework_example.helpers.pages.main_page import MainPage


class ElementsPage(LeftMenuCompositeElement):

    url = MAIN_URL + '/elements'
    text_box_menu_locator = '//*[@id="item-0" and .="Text Box"]'

    # '//*[@for="tree-node-desktop"]/ancestor::li[contains(@class, "rct-node-parent") and child::*[.="Desktop"]]/ol//*[@class="rct-title"]'

    def open_page(self,):
        self.driver.go_to(self.url)

    def open_page_by_left_panel(self, element_locator):
        self.open_accordion_group(self.elements_group_button)
        self.open_page_by_left_menu(element_locator)
        # return self

    def check_url(self, url_example):
        assert self.driver.driver.current_url == url_example
