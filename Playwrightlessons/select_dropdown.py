from playwright.sync_api import sync_playwright, expect

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto(url="https://demo.automationtesting.in/Register.html")
#     skills_dropdown = page.locator(selector="select#Skills")
#     skills_dropdown.select_option(label="C++")
#     yearbox_dropdown = page.select_option(selector="select#yearbox", label="1996")
#     page.wait_for_timeout(3000)
#     browser.close()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url="https://selenium08.blogspot.com/2019/11/dropdown.html")
    dropdowns = page.locator(selector="select[name=country]>option")
    page.wait_for_timeout(3000)
    print(dropdowns.count())
    for i in dropdowns.all_inner_texts():
        print(i)
    print(dropdowns.last.inner_text())
    browser.close()
