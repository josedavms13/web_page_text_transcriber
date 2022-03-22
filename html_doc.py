from typing import List

from selenium.webdriver.remote.webelement import WebElement

from docs.sheet import Sheet


def parse_html_content(sheet: Sheet, items: List[WebElement]):

    for item in items:
        if item.tag_name == "h2":
            sheet.type_sub_title(item.text)
        if item.tag_name == "p":
            sheet.type_paragraph(item.text)