from test_framework_example.browser import Browser
from test_framework_example.constants import MAIN_URL
from test_framework_example.helpers.pages.base_page import BasePage


class MainPage:

    def __init__(self):
        self.driver = Browser()
        self.elements_card_locator = '//*[@class="card-body" and .="Elements"]'
        self.forms_card_locator = '//*[@class="card-body" and .="Forms"]'
        self.alerts_frame_card_locator = '//*[@class="card-body" and .="Alerts, Frame & Windows"]'
        self.widgets_card_locator = '//*[@class="card-body" and .="Widgets"]'
        self.interactions_card_locator = '//*[@class="card-body" and .="Interactions"]'
        self.book_store_locator = '//*[@class="card-body" and .="Book Store Application"]'

    def open_page_by_card(self, card_locator):
        card_element = self.driver.find_by_xpath(card_locator)
        card_element.click()

        self.driver.driver.find_elements()

        return self

