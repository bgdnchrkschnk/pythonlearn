from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium_learning.selenium_test_task.fixtures import *
from time import sleep


def test_page_is_correct(chrome_browser):
    actions = ActionChains(chrome_browser)
    chrome_browser.get("https://google.com")
    sleep(2)
    search_line = chrome_browser.find_element(By.CSS_SELECTOR, ".gLFyf")
    search_line.send_keys("milan star")
    actions\
        .key_down(Keys.ENTER)\
        .key_up(Keys.ENTER)\
        .perform()
    sleep(5)
    link = chrome_browser.find_element(By.XPATH, "//h3[contains(text(), 'Тверк')]")
    actions\
        .scroll_to_element(element=link)\
        .pause(5)\
        .perform()