from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url="https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html")

    sheet = page.query_selector(selector="#customers")

    sheet_raws = sheet.query_selector_all(selector="tr")
    sheet_columns = sheet.query_selector_all(selector="td")

    for raw in sheet_raws:
        cells = raw.query_selector_all("td")
        [print(cell.text_content()) for cell in cells]


    # [print(column.text_content()) for column in sheet_columns]
