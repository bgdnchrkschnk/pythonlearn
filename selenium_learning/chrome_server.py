from selenium.webdriver import Remote, DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep

chrome_options = Options()


chrome_browser = Remote(command_executor= 'http://192.168.0.101:4444/wd/hub', options=chrome_options)
chrome_browser.get("https://google.com")
print(chrome_browser.title)
sleep(5)
chrome_browser.quit()