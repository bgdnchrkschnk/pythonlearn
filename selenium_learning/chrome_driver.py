from time import sleep

from selenium import webdriver

# Configuring Chrome browser
from selenium.webdriver.chrome.options import Options

#Configuring other browsers (Remote)
from selenium.webdriver import DesiredCapabilities

#Setting browser capabilities (REMOTE)
# capabilities = DesiredCapabilities.CHROME
# capabilities['platform'] = "MAC"
# capabilities['acceptInsecureCerts'] = True

#Initialize options for Google Chrome (Local only)
chrome_options = Options()
#headless - processing in background mode
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")

#ChromeDriver initialize
# chrome_browser = webdriver.Chrome(options=chrome_options, desired_capabilities=capabilities)
chrome_browser = webdriver.Chrome(options=chrome_options)

chrome_browser.maximize_window()
chrome_browser.get("https://www.github.com")
sleep(1)
chrome_browser.get("https://about.gitlab.com/")
chrome_browser.back()
sleep(1)
chrome_browser.forward()
print(chrome_browser.current_url)
print(chrome_browser.title)
sleep(1)

chrome_browser.quit()




