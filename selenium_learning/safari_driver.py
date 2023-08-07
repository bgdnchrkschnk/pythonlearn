from selenium import webdriver
# from selenium.webdriver import Remote, DesiredCapabilities
from time import sleep
from selenium.webdriver.safari.options import Options

#Initialize options for Google Chrome (Local only)
safari_options = Options()
#headless - processing in background mode
safari_options.add_argument("--disable-extensions")



safari_browser = webdriver.Safari()
safari_browser.maximize_window()
safari_browser.get("https://google.com")
sleep(2)
safari_browser.get("https://ask.fm")
sleep(2)
safari_browser.back()
sleep(2)
safari_browser.forward()
sleep(2)
safari_browser.refresh()
print("Done!")
safari_browser.quit()

#REMOTE
# safari_browser = Remote(command_executor="http://192.168.0.101:4444", desired_capabilities=DesiredCapabilities.SAFARI)
# safari_browser.get("https://google.com")
# safari_browser.get("https://ask.fm")
# safari_browser.back()
# safari_browser.forward()
# sleep(5)
# safari_browser.quit()

