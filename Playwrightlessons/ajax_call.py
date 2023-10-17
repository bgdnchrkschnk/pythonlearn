from pprint import pprint

from playwright.sync_api import sync_playwright

def handle_rejex(response):
    if "https://www.plus2net.com/php_tutorial/dd-ajax.php?" in response.url:
        status = response.status
        data = response.text()
        print(f"status_code: {status}, data: {data}")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url="https://www.plus2net.com/php_tutorial/ajax_drop_down_list-demo.php")
    page.select_option(value="2", selector="#s1")

    page.on("response", lambda response: handle_rejex(response))

    page.wait_for_timeout(3000)
    browser.close()




