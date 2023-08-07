import pytest
from time import sleep

def test_task(chrome_browser):
    chrome_browser.get("https://github.com/")
    print(chrome_browser.title)
    sleep(2)
    assert chrome_browser.title == "GitHub: Let’s build from here · GitHub"
    assert chrome_browser.current_url == "https://github.com/"
    chrome_browser.get("https://ask.fm/")
    sleep(2)
    assert chrome_browser.title == "Ask and Answer - ASKfm"
    assert chrome_browser.current_url == "https://ask.fm/"
    chrome_browser.back()
    sleep(5)
    assert chrome_browser.title == "GitHub: Let’s build from here · GitHub"
    assert chrome_browser.current_url == "https://github.com/"
    chrome_browser.forward()
    sleep(5)
    assert chrome_browser.title == "Ask and Answer - ASKfm"
    assert chrome_browser.current_url == "https://ask.fm/"
