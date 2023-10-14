from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url="https://demo.automationtesting.in/Register.html")
    female_option = page.locator(selector="input[value=FeMale]")
    checkbox = page.locator(selector="#checkbox1")
    checkbox.check()
    female_option.check()
    if female_option.is_checked() and checkbox.is_checked():
        print("Success!")
    else:
        print("Options are not checked!")
    page.wait_for_timeout(3000)
    browser.close()
