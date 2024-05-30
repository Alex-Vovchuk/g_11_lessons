from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from test_framework_example.constants import MAIN_URL


class Browser(object):

    service = Service(executable_path=".//chromedriver.exe")
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=service)
    driver.set_window_size(1920, 1080)

    def go_to(self, url=MAIN_URL):
        self.driver.get(url)

    def find_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)
