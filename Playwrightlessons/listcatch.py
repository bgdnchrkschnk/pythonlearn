from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url="https://demo.automationtesting.in/Selectable.html")


    # all_block = page.locator("#Default")
    # print(all_block.text_content())


    # elements = page.query_selector_all(selector="b")
    # for i in elements:
    #     print(i.text_content())
    try:
        elements = page.query_selector_all(selector="a")
        for i in elements:
            print(i.get_attribute(name="href"))

        element = page.locator(selector=".twitter")
        print(element.get_attribute(name="target"))
    except Exception as e:
        print(str(e))
    finally:
        print("The end")
    page.wait_for_timeout(3000)

    context.close()
