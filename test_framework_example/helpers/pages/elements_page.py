from test_framework_example.browser import Browser
from test_framework_example.constants import MAIN_URL
from test_framework_example.helpers.pages.base_page import BasePage
from test_framework_example.helpers.pages.composite_elements import LeftMenuCompositeElement
from test_framework_example.helpers.pages.main_page import MainPage


class ElementsPage:

    def __init__(self):
        self.url = MAIN_URL + '/elements'
        self.driver = Browser()
        self.text_box_menu_locator = '//*[@id="item-0" and .="Text Box"]'
        self.composite = LeftMenuCompositeElement(self.driver)

        # '//*[@for="tree-node-desktop"]/ancestor::li[contains(@class, "rct-node-parent") and child::*[.="Desktop"]]/ol//*[@class="rct-title"]'

    def open_page_by_left_panel(self, element_locator):
        self.composite.open_accordion_group(self.composite.elements_group_button)
        self.composite.open_page_by_left_menu()
        # return self

    def check_url(self, url_example):
        assert self.driver.driver.current_url == url_example
        # return self

    def click_to_logo(self, ):
        logo_button = self.driver.find_by_xpath(page_locator)
        logo_button.click()

