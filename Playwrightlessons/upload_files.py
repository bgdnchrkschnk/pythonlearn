from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url="https://demo.automationtesting.in/FileUpload.html")

    page.locator("#input-4").set_input_files("./screenshot.png")
    page.wait_for_timeout(3000)

