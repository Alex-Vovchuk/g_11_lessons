import pytest

from test_framework_example.helpers.data_registry import DataRegistry
from test_framework_example.helpers.factoryj import PageFactory
from test_framework_example.helpers.pages.FormPage import FormPage
from test_framework_example.helpers.pages.composite_elements import LeftMenuCompositeElement
from test_framework_example.helpers.pages.elements_page import ElementsPage
from test_framework_example.helpers.pages.main_page import MainPage
from test_framework_example.helpers.pages.value_object import UserCredentials, Builder



@pytest.fixture
def get_factory():
    return PageFactory()


class TestMainPage:

    def test_open_element_card(self, get_factory):
        main_page = get_factory.get_page('Main')
        main_page.open().open_page_by_card(main_page.elements_card_locator)

        assert main_page.driver.current_url == 'https://demoqa.com/elements'

    def test_chain_of_invocations(self):
        left_menu = LeftMenuCompositeElement()
        left_menu.open_page_by_left_menu()
        elements_page.open().check_url('https://demoqa.com/elements').click_to_logo(logo_locator)

    def test_form(self):
        credentials = UserCredentials(first_name='John', last_name='Doe',)
        form_page = FormPage()
        form_page.fill_form_fields(credentials)

    def test_form_second(self):
        credentials_builder = Builder()
        new_user = (credentials_builder.add_string('first_name', 'John').add_boolean()
                    .add_array().add_string().add_boolean().add_array().build())

        form_page = FormPage()
        form_page.fill_form_fields(new_user)

    def test_form_third(self):
        credentials = DataRegistry()
        new_user = credentials.add_first_name().add_last_name()
        credentials.is_first_name_unique(new_user)

        form_page = FormPage()
        form_page.fill_form_fields(new_user)
    def test_form_third(self):
        credentials = DataRegistry()
        new_user = credentials.add_first_name().add_last_name()
        credentials.is_first_name_unique(new_user)

        form_page = FormPage()
        form_page.fill_form_fields(new_user)
