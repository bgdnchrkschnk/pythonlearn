from playwright.sync_api import sync_playwright

with sync_playwright() as driver:
    browser = driver.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url="https://www.ask.fm/")
    sign_in_button = page.locator("p>[data-action=ClickTrack]")
    sign_in_button.click()
    page.wait_for_timeout(1000)
    username_input = page.locator("#user_name")
    password_input = page.locator("#user_password")
    username_input.type("rbninves@gmail.com", delay=0.3)
    password_input.type("rube783y78")
    sign_in_button = page.locator("[type=submit]")
    sign_in_button.click()
    print(page.title())
    page.wait_for_timeout(3000)
    browser.close()