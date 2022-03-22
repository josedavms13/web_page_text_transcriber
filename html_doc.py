from typing import List

from selenium.webdriver.remote.webelement import WebElement

from docs.sheet import Sheet


def parse_html_content(sheet: Sheet, items: List[WebElement]):
    ul_collections = """"""
    for item in items:
        if item.tag_name == "h2":
            sheet.type_sub_title(item.text)
            if len(ul_collections) > 0:
                sheet.type_as_list(ul_collections)
            ul_collections = """"""

        if item.tag_name == "p":
            sheet.type_paragraph(item.text)
            if len(ul_collections) > 0:
                sheet.type_as_list(ul_collections)
            ul_collections = """"""

        if item.tag_name == "li":
            ul_collections += f"   - {item.text} \n"


