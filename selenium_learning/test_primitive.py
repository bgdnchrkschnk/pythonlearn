import pytest
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import os
import random
import string
from selenium_learning.selenium_test_task.fixtures import *

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
    assert chrome_browser.title == "Google", chrome_browser.get_screenshot_as_file("/Users/bgdnchrkschnk/Documents/title.png")
    # check.is_true(chrome_browser.title == "Googled", "Test failed")


# def test_ebay_search_bar(chrome_browser):
#     chrome_browser.get("https://ebay.com/")
#     sleep(2)
#     search_bar = chrome_browser.find_element(By.CSS_SELECTOR, "input.gh-tb")
#     search_button = chrome_browser.find_element(By.ID, "gh-btn")
#     search_bar.send_keys("Iphone 14")
#
#     # screen = search_bar.screenshot_as_png
#     # with open(os.path.join("/Users/bgdnchrkschnk/Documents/", "test.png"), "wb") as pp:
#     #     pp.write(screen)
#
#     search_bar.clear()
#     search_bar.send_keys("iPhone 15")
#     check.is_true(search_bar.get_attribute("autocorrect")=="off", "Fail")
#     search_button.click()
#     sleep(2)
#     # chrome_browser.get_screenshot_as_file(f"/Users/bgdnchrkschnk/Documents/, {'' .join(random.choices(string.ascii_letters, k=random.randint(1,20)))}.png")
#
#     # png_screenshot = chrome_browser.get_screenshot_as_png()
#     # with open(os.path.join("/Users/bgdnchrkschnk/Documents/", "png.png"), "wb") as pp:
#     #     pp.write(png_screenshot)
#     items = chrome_browser.find_elements(By.CSS_SELECTOR, "li.s-item")
#     assert len(items), "No found items :("
#     for item in items:
#         # item.screenshot(os.path.join("/Users/bgdnchrkschnk/Documents/", "1.png"))
#         # item.screenshot("/Users/bgdnchrkschnk/Documents/1.png")
#         # item.screenshot(os.path.join("/Users/bgdnchrkschnk/Documents/", f"{'' .join(random.choices(string.ascii_letters, k=random.randint(1,20)))}.png"))
#         assert item.is_displayed(), "NOT DISPLAYED!"
#         assert item.is_enabled(), "NOT ENABLED!"
#         assert not item.is_selected(), "SELECTED"
#     assert chrome_browser.find_element(By.CSS_SELECTOR, "input.gh-tb") == chrome_browser.find_element(By.ID, "gh-ac")


def test_joom(chrome_joom:Chrome):
    search_bar = chrome_joom.find_element(By.CSS_SELECTOR, "input.input___QjcpQ")
    sleep(2)
    cross = chrome_joom.find_element(By.CSS_SELECTOR, "button.close___ukMoE")
    cross.click()
    sleep(2)
    check.is_true(search_bar.is_displayed(), "Fail")
    check.is_true(search_bar.is_enabled(), "Fail")
    search_bar.send_keys("swiss tool")
    sleep(2)