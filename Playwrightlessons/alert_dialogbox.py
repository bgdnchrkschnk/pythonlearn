from playwright.sync_api import sync_playwright

l = list()

def handle_dialog(dialog):
    l.append(dialog.message)
    dialog.accept()
    print(l)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url="https://demo.automationtesting.in/Alerts.html")

    page.locator(selector="a[href='#CancelTab']").click()
    page.wait_for_timeout(1000)
    # page.on("dialog", lambda dialog: dialog.accept())
    # page.on("dialog", lambda dialog: dialog.dismiss())
    page.on("dialog", handle_dialog)
    page.locator(selector="button.btn-primary").click()
    page.wait_for_timeout(3000)
    browser.close()
