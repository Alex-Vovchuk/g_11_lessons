from test_framework_example.helpers.pages.elements_page import ElementsPage
from test_framework_example.helpers.pages.main_page import MainPage


class TestMainPage:

    def test_open_element_card(self):
        main_page = MainPage()
        main_page.open().open_page_by_card(main_page.elements_card_locator)

        assert main_page.driver.current_url == 'https://demoqa.com/elements'

    def test_chain_of_invocations(self):
        elements_page = ElementsPage()
        elements_page.open().check_url('https://demoqa.com/elements').click_to_logo(logo_locator)




