from real_project_example.helper.pages.buttons_page import ButtonsPage
from faker import Faker

from real_project_example.helper.pages.text_boxes_page import TextBoxesPage


class TestTextBoxesPage:

    def test_fill_text_boxes_correct_info(self):
        faker = Faker()
        text_boxes_page = TextBoxesPage()
        text_boxes_page.open_page()

        name_value = faker.name()
        text_boxes_page.set_value_input(text_boxes_page.name_input, name_value)
        text_boxes_page.set_value_input(text_boxes_page.email_input, faker.email())
        text_boxes_page.set_value_input(text_boxes_page.current_address_input, faker.address())
        text_boxes_page.set_value_input(text_boxes_page.permanent_address_input, faker.address())

        text_boxes_page.click(text_boxes_page.submit_button)

        assert text_boxes_page.is_displayed(text_boxes_page.name_message)
        assert text_boxes_page.is_displayed(text_boxes_page.email_message)
        assert text_boxes_page.is_displayed(text_boxes_page.current_address_message)
        assert text_boxes_page.is_displayed(text_boxes_page.permanent_address_message)

        assert f'Name:{name_value}' == text_boxes_page.get_text(text_boxes_page.name_message)
