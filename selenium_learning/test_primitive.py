import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")

@pytest.fixture
def chrome_browser():
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_page_is_correct(chrome_browser):
    chrome_browser.get("https://google.com")
    sleep(2)
    chrome_browser.get("https://ask.fm")
    sleep(2)
    chrome_browser.get("https://google.com")
    sleep(2)
    chrome_browser.refresh()
    assert chrome_browser.title == "Googled", "Test failed"