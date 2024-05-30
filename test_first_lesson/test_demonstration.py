import logging
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path=".//chromedriver.exe")
driver = webdriver.Chrome(service=service)

WAIT_TIME = 10


def wait_for_visible(driver, element, timeout=WAIT_TIME):
    return WebDriverWait(driver, timeout, poll_frequency=1.5, ignored_exceptions=[TimeoutException]).until_not(EC.number_of_windows_to_be(2))


def test_something():
    driver.implicitly_wait(10)
    driver.get("https://demoqa.com/automation-practice-form")
    element_to_hover = driver.find_element(By.CSS_SELECTOR, "#firstName")

    wait_for_visible(driver, element_to_hover, timeout=20)

    element_to_hover.send_keys("I wan't to send this")
    driver.find_element(By.CSS_SELECTOR, "#mainMenu")

    