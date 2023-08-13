import sys

import selenium
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from time import sleep


driver = selenium.webdriver.Chrome()
driver.get(url="https://bing.com/")


# Initialize ActionChains
actions = ActionChains(driver)

search_field = driver.find_element(By.CSS_SELECTOR, "#sb_form_q")
search_button = driver.find_element(By.CSS_SELECTOR, "circle[stroke='#007DAA']")
sleep(3)


# Actions can be queeued in a chain pattern

actions.click(on_element=search_field).pause(3).send_keys_to_element(search_field, "python+selenium").click(on_element=search_button).perform()
sleep(5)
selenium_link = driver.find_element(By.CSS_SELECTOR, ".b_topTitle>a")

assert selenium_link.is_displayed()
assert selenium_link.is_enabled()
sleep(2)

image_search_button = driver.find_element(By.CSS_SELECTOR, "#sbi_b")
sleep(2)

image_search_button.click()

image_search_box = driver.find_element(By.CSS_SELECTOR, ".dpnmpn")

actions.drag_and_drop(source=selenium_link, target=image_search_box).perform()

sleep(3)

command_key = Keys.COMMAND if sys.platform == "darwin" else Keys.CONTROL

actions.key_down(command_key)\
    .send_keys('a')\
    .key_up(command_key)\
    .key_down(command_key)\
    .send_keys('c')\
    .key_up(command_key)\
    .pause(5)\
    # .drag_and_drop(source=selenium_link, target=search_button) \
    .drag_and_drop_by_offset(source=selenium_link, xoffset=100, yoffset=100) \
    .perform()

Actions can be queeued one by one

actions.click(on_element=search_field)
sleep(1)
actions.send_keys_to_element(search_field, "python + selenium")
sleep(1)
# actions.click(on_element=search_button)
actions.key_down(Keys.ENTER)
actions.key_up(Keys.ENTER)
actions.perform()
sleep(5)
selenium_link = driver.find_element(By.CSS_SELECTOR, ".b_topTitle>a")
sleep(3)
assert selenium_link.is_displayed()
assert selenium_link.is_enabled()

driver.quit()