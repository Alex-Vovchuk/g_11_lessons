from test_framework_example.browser import Browser


class FormPage:

    def __init__(self):
        self.driver = Browser()
        self.first_name_locator = '//*[@class="card-body" and .="Elements"]'
        self.last_name_input = '//*[@class="card-body" and .="Forms"]'
        self.date_of_birth_calendar = '//*[@class="card-body" and .="Alerts, Frame & Windows"]'
        self.male_radio_btn = '//*[@class="card-body" and .="Widgets"]'
        self.female_radio_btn = '//*[@class="card-body" and .="Interactions"]'
        self.book_store_locator = '//*[@class="card-body" and .="Book Store Application"]'

    def fill_form_fields(self, credentials):
        first_name_input = self.driver.find_by_xpath(self.first_name_locator)
        first_name_input.clear()
        first_name_input.send_keys(credentials.first_name)

        first_name_input = self.driver.find_by_xpath(self.first_name_locator)
        first_name_input.clear()
        first_name_input.send_keys(credentials.first_name)
        first_name_input = self.driver.find_by_xpath(self.first_name_locator)
        first_name_input.clear()
        first_name_input.send_keys(credentials.first_name)
        first_name_input = self.driver.find_by_xpath(self.first_name_locator)
        first_name_input.clear()
        first_name_input.send_keys(credentials.first_name)
