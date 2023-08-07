# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from time import sleep
#
# #Initialize options for Firefox (Local only)
# firefox_options = Options()
# firefox_options.add_argument("--disable-extensions")
#
#
#
# firefox_browser = webdriver.Firefox(options=firefox_options)
# firefox_browser.get("https://google.com.ua")
# firefox_browser.maximize_window()
# sleep(5)
# firefox_browser.quit()

from selenium.webdriver import Remote, DesiredCapabilities
from selenium.webdriver.firefox.options import Options

firefix_options = Options()

firefox_browser = Remote(command_executor= 'http://192.168.0.101:4444/wd/hub/', options=firefix_options)

