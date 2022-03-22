from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from web.base_page import BasePage


class WebPage(BasePage):
    def __init__(self, url: str):
        super(WebPage, self).__init__(url)
        print("Opening web page")
        self.driver.maximize_window()
        input("Acepta las cookies y preciona enter")
        self.restore_window_size()

    def get_main_titles(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div h1")))

    def get_content(self) -> List[WebElement]:
        WebDriverWait(self.driver, 10)\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, "div h2 ~ p, div h2")))
        return self.driver.find_elements(By.CSS_SELECTOR, "div h2 ~ p, div h2")


