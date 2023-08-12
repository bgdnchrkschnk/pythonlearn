from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

driver.get("https://google.com.ua")

# Find element by
# driver.find_element(By.ID, "a.gb_y")
# driver.find_element(By.XPATH, "a.gb_y")
# driver.find_element(By.LINK_TEXT, "a.gb_y")
# driver.find_element((By.PARTIAL_LINK_TEXT), "a.gb_y")
# driver.find_element(By.TAG_NAME, "a")
# driver.find_element(By.CLASS_NAME, "a.gb_y")
# try:
#     driver.find_element(By.CSS_SELECTOR, "a.gb_y")
# except:
#     print("Error!")


# Find elements by - returns a list of found elements
# driver.find_elements(By.ID, "a.gb_y")
# driver.find_elements(By.XPATH, "a.gb_y")
# driver.find_elements(By.LINK_TEXT, "a.gb_y")
# driver.find_elements((By.PARTIAL_LINK_TEXT), "a.gb_y")
# print(driver.find_elements(By.TAG_NAME, "a"))
# driver.find_elements(By.CLASS_NAME, "a.gb_y")
# driver.find_elements(By.CSS_SELECTOR, "a.gb_y")
sleep(2)
driver.close()