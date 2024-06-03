from selenium.webdriver.common.by import By

from test_framework_example.browser import Browser
from test_framework_example.constants import MAIN_URL


class BasePage:

    def __init__(self):
        self.driver = Browser()
        self.left_menu_locator = "adlkfsg;kladjf"


    def open(self):
        self.driver.go_to(url=MAIN_URL)
        return self

    def click(self):
        self.driver.find_by_xpath().click()

    def open_left_menu(self, button):
        alerts_button = self.driver.find_by_xpath(self.left_menu_locator)
