from test_framework_example.helpers.pages.base_page import BasePage
from test_framework_example.helpers.pages.elements_page import ElementsPage
from test_framework_example.helpers.pages.main_page import MainPage


class PageFactory:

    @staticmethod
    def get_page(page_name):
        match page_name:
            case 'Main':
                return MainPage()
            case 'Elements':
                return ElementsPage()
            case 'Base':
                return BasePage()

        # if page_name == 'Main':
        #     return MainPage()
        # elif page_name == 'Elements':
        #     return ElementsPage()
