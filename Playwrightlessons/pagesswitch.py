from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url="https://demo.automationtesting.in/Windows.html")
    print(page.title())
    page.locator(selector="//button[contains(text(), '  click  ')]").click()
    page.wait_for_timeout(3000)
    total_pages = context.pages
    print(len(total_pages))
    for page in total_pages:
        print(page)
    new_page = total_pages[1]
    new_page.bring_to_front()
    new_page.wait_for_timeout(3000)
    print(new_page.title())
    # total_pages[0].bring_to_front()
    print(total_pages[0].title())
    new_page.close()
    page.wait_for_timeout(3000)
    browser.close()