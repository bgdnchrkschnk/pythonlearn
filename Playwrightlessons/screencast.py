import os

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir="./screencasts/")
    page = context.new_page()
    page.goto(url="https://ask.fm/login")
    page.locator("#user_name").type("bgdnchrkschnk")
    page.locator("#user_password").type(os.environ['askfm_pw'])
    page.screenshot(timeout=1000, path="./screenshots/login.png")
    page.locator("input[type=submit]").click()
    page.wait_for_timeout(2000)
    page.screenshot(path="./screenshots/private_cabinet.png")
    page.wait_for_timeout(3000)
    context.close()

