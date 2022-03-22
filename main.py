from docs.sheet import Sheet
from web.web_page import WebPage
from html_doc import parse_html_content

print("\t====Trancriptor de paginas a texto==== Solo funciona con la de omnilife por ahora")

page_url = "https://vendiendo.co/blogs/omniplus-supreme-omnilife-beneficios/"

sheet = Sheet()

web_page = WebPage(page_url)
main_titles = web_page.get_main_titles()
sheet.type_title(main_titles.text)
input("TODO LISTO PRESIONA ENTER")
items = web_page.get_content()
parse_html_content(sheet, items)

sheet.save(input("Pon el nombre del archivo: "))