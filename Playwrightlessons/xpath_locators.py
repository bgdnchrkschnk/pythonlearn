from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url="https://www.4club.com.ua")
    search_input = page.locator(selector="//*[@id='search_input']")
    search_button = page.locator(selector="//button[@class='ty-search-magnifier']")
    search_input.type("Neumann TLM 103")
    search_button.click()
    page.wait_for_timeout(3000)
    browser.close()