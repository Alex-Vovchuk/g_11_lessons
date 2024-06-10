from real_project_example.helper.pages.base_page import BasePage, MAIN_URL
from test_framework_example.browser import Browser


class FormPage(BasePage):

    url = MAIN_URL + '/automation-practice-form'
    first_name_locator = '//*[@id="firstName"]'
    last_name_input = '//*[@id="lastName"]'
    email_input = '//*[@id="userEmail"]'
    male_button = '//*[@id="gender-radio-1"]/..'
    female_button = '//*[@id="gender-radio-2"]/..'
    other_gender_button = '//*[@id="gender-radio-3"]/..'
    phone_number_input = '//*[@id="userNumber"]'
    subject_input = '//*[@id="subjectsContainer"]'

    sport_checkbox = '//*[@id="hobbies-checkbox-1"]/..'
    reading_checkbox = '//*[@id="hobbies-checkbox-2"]/..'
    music_checkbox = '//*[@id="hobbies-checkbox-3"]/..'

    current_address = '//*[@id="currentAddress"]/..'
    state_dropdown = '//*[@id="state"]/..'

    submit_button = '//*[@id="submit"]'

    def open_page(self,):
        self.driver.go_to(self.url)

