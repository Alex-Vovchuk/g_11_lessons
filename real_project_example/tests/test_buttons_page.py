from real_project_example.helper.pages.buttons_page import ButtonsPage
from selenium import webdriver


class TestButtonsPage:

    def test_double_click_button(self):
        button_page = ButtonsPage()
        button_page.open_page()

        button_page.double_click_element(button_page.double_click_button)
        assert button_page.is_displayed(button_page.double_click_message)
        assert not button_page.is_displayed(button_page.right_click_message)
        assert not button_page.is_displayed(button_page.dynamic_click_message)

    def test_right_click_button(self):
        button_page = ButtonsPage()
        button_page.open_page()

        button_page.right_click_element(button_page.right_click_button)
        assert button_page.is_displayed(button_page.right_click_message)

    def test_simple_click_button(self):
        button_page = ButtonsPage()
        button_page.open_page()

        button_page.find_by_xpath(button_page.double_click_button).click()
        assert button_page.is_displayed(button_page.dynamic_click_message)

