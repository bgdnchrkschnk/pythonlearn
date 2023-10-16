import json

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.redbus.in/")

    my_cookies = context.cookies()
    # print(my_cookies)

    context.clear_cookies()

    print(context.cookies())

    # with open("savedcookies.json", "w") as c:
    #     c.write(json.dumps(context.cookies()))
    #
    #
    # with open("cooks.json") as c:
    #     cookies = json.loads(c.read())
    #     for cookie in cookies:
    #         context.add_cookies(cookie)
    #     print(my_cookies)

