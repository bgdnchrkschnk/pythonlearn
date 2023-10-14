from playwright.sync_api import sync_playwright

with sync_playwright() as driver:
    browser = driver.chromium.launch()
    page = browser.new_page()
    page.goto(url="https://www.ask.fm/")
    print(page.title())
    page.wait_for_timeout(3000)
    browser.close()