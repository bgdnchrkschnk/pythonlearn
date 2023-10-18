from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url="https://demo.imacros.net/Automate/Downloads")

    with page.expect_download() as download_data:
        page.locator("//a[@href='/Content/Download2.zip']").click()
    download = download_data.value

    download.save_as(path="./files/" + download.suggested_filename)

    page.wait_for_timeout(3000)

