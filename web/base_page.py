
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    def __init__(self, url: str):
        self._url = url
        self._init_size = [800, 1000]
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        self.driver.get(url)
        self.restore_window_size()

    def exit(self):
        self.driver.close()

    def restore_window_size(self):
        self.driver.set_window_size(self._init_size[0], self._init_size[1])

    def go_to_page(self, url: str):
        self.driver.get(url)

