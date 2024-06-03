class LeftMenuCompositeElement:
    def __init__(self, driver):
        self.driver = driver
        self.elements_group_button = '//*[@class="header-text" and .="Elements"]/..'
        self.text_box_button = '//*[@class="header-text" and .="Elements"]/ancestor::*[@class="element-group"]//*[@id="item-0"]'
        self.check_box_button = '//*[@class="header-text" and .="Elements"]/ancestor::*[@class="element-group"]//*[@id="item-1"]'
        self.radio_button_button = '//*[@class="header-text" and .="Elements"]/ancestor::*[@class="element-group"]//*[@id="item-2"]'
        self.web_tables_button = '//*[@class="header-text" and .="Elements"]/ancestor::*[@class="element-group"]//*[@id="item-3"]'

    def open_accordion_group(self, group_locator):
        element = self.driver.find_by_xpath(group_locator)
        self.driver.wait_for_clickable(element)
        element.click()

    def open_page_by_left_menu(self, menu_name):
        pass

