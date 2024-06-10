from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os


class Browser(object):

    current_dir = os.path.dirname(os.path.abspath(__file__))

    service = Service(executable_path=os.path.join(current_dir, "chromedriver.exe"))
    driver = webdriver.Chrome(service=service)
    driver.set_window_size(1920, 1080)

