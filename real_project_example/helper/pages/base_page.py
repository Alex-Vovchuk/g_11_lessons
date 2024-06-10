
from selenium.common import StaleElementReferenceException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from real_project_example.browser import Browser


MAIN_URL = 'https://demoqa.com'
BASE_TIMEOUT = 10


class BasePage:

    def __init__(self):
        self.browser = Browser()
        self.driver = self.browser.driver

    def go_to(self, url=MAIN_URL):
        self.driver.get(url)
        return self

    def find_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def find_elements_by_xpath(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)

    def wait_for_clickable(self, locator, timeout=BASE_TIMEOUT):
        self._wait_for(EC.element_to_be_clickable, locator, timeout)
        return self

    def wait_for_visible(self, locator, timeout=BASE_TIMEOUT):
        self._wait_for(EC.visibility_of_element_located, locator, timeout)
        return self

    def wait_for_present(self, locator, timeout=BASE_TIMEOUT):
        self._wait_for(EC.presence_of_element_located, locator, timeout)
        return self

    def get_current_url(self):
        return self.driver.current_url

    def refresh(self):
        self.driver.refresh()
        return self

    def wait_for_element_invisible(self, locator, timeout=BASE_TIMEOUT):
        self._wait_for(EC.invisibility_of_element_located, locator, timeout)

    def _wait_for(self, expected_condition, locator, timeout):
        try:
            WebDriverWait(self.driver, timeout).until(
                expected_condition((By.XPATH, locator)))
        except StaleElementReferenceException:
            self._wait_for(expected_condition, locator, timeout)

    def wait_for_action(self, action_method, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            action_method, message='Action is not happen')
        return self

    def get_el_attribute(self, locator, attribute_name):
        try:
            return self.find_by_xpath(locator).get_attribute(attribute_name)
        except StaleElementReferenceException:
            return self.find_by_xpath(locator).get_attribute(attribute_name)

    def set_value_input(self, locator, value):
        self.find_by_xpath(locator).send_keys(value)
        return self

    def double_click_element(self, locator):
        self.wait_for_clickable(locator)
        element = self.find_by_xpath(locator)
        ActionChains(self.driver).double_click(element).perform()

    def right_click_element(self, locator):
        self.wait_for_clickable(locator)
        element = self.find_by_xpath(locator)
        ActionChains(self.driver).context_click(element).perform()

    def is_displayed(self, locator):
        try:
            self.wait_for_visible(locator, timeout=2)
            element = self.find_by_xpath(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    def click(self, locator):
        try:
            self.wait_for_clickable(locator)
            self.find_by_xpath(locator).click()
        except ElementClickInterceptedException:
            self.driver.execute_script(f'window.scrollBy(0, {400});')
            self.find_by_xpath(locator).click()

    def get_text(self, locator):
        self.wait_for_present(locator)
        return self.find_by_xpath(locator).text

    def scroll_to_element(self, locator):
        element = self.find_by_xpath(locator)


