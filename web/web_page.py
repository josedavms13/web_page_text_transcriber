from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web.base_page import BasePage


class WebPage(BasePage):
    def __init__(self, url: str):
        super(WebPage, self).__init__(url)
        print("Opening web page")
