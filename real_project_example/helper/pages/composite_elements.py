from real_project_example.helper.pages.base_page import BasePage


class LeftMenuElement(BasePage):

    elements_group_button = '//*[@class="header-text" and .="Elements"]/..'
    text_box_button = '//*[@class="header-text" and .="Elements"]/ancestor::*[@class="element-group"]//*[@id="item-0"]'
    check_box_button = '//*[@class="header-text" and .="Elements"]/ancestor::*[@class="element-group"]//*[@id="item-1"]'
    radio_button_button = '//*[@class="header-text" and .="Elements"]/ancestor::*[@class="element-group"]//*[@id="item-2"]'
    web_tables_button = '//*[@class="header-text" and .="Elements"]/ancestor::*[@class="element-group"]//*[@id="item-3"]'

    def open_accordion_group(self, group_locator):
        element = self.driver.find_by_xpath(group_locator)
        self.driver.wait_for_clickable(element)
        element.click()

    # def open_page_by_left_menu(self, menu_name):
    #     pass
    #
    #     elements_group_button = '//*[@class="header-text" and .="Elements"]/..'
    #     text_box_button = '//*[@class="header-text" and .="Elements"]/ancestor::*[@class="element-group"]//*[@id="item-0"]'
    #     check_box_button = '//*[@class="header-text" and .="Elements"]/ancestor::*[@class="element-group"]//*[@id="item-1"]'
    #     radio_button_button = '//*[@class="header-text" and .="Elements"]/ancestor::*[@class="element-group"]//*[@id="item-2"]'
    #     web_tables_button = '//*[@class="header-text" and .="Elements"]/ancestor::*[@class="element-group"]//*[@id="item-3"]'