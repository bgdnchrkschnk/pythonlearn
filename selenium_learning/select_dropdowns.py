from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from time import sleep


# LECTURE
driver = webdriver.Chrome()
driver.maximize_window()

def test():
    driver.get("https://docs.python.org/3/library/pydoc.html")
    sleep(2)
    element = Select(driver.find_element(By.CSS_SELECTOR, "#language_select"))
    sleep(2)
    element.select_by_value("fr")
    sleep(5)
    el2 = driver.find_element(By.CSS_SELECTOR, "button.lang-btn")
    assert el2.text == "pydoc — Générateur de documentation et système d’aide en ligne", "Text wrong"
    driver.quit()

if __name__ == '__main__':
    test()

