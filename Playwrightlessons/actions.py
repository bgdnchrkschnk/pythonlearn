from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(url="https://demo.automationtesting.in/Selectable.html")

    # page.get_by_text(text="SwitchTo").hover()
    # page.get_by_text(text="SwitchTo").dblclick()
    # page.get_by_text(text="SwitchTo").click(button="right")
    #
    # #Shift Click
    # page.get_by_text(text="SwitchTo").click(modifiers=["Shift"])
    #
    # # A-Z, 0-9, F1-F12, Special characters, ArrowRight, ArrowDown, PageUp, Enter, Control, Command
    # page.get_by_text(text="SwitchTo").press("A")
    # page.get_by_text(text="SwitchTo").press("$")

    page.keyboard.press(key="Meta+A")

    page.wait_for_timeout(3000)

    context.close()







    page.wait_for_timeout(timeout=3000)
