from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from time import sleep



driver = webdriver.Chrome()
driver.maximize_window()

def test():
    driver.get("https://ucoz.ru/")
    sleep(2)
    element = Select(driver.find_element(By.CSS_SELECTOR, "div.open"))
    sleep(2)
    element.select_by_index("2")
    sleep(5)
    el2 = driver.find_element(By.CSS_SELECTOR, "button.lang-btn")
    assert el2.text == "Python 2.7.18 documentation", "Text wrong"
    driver.quit()

if __name__ == '__main__':
    test()