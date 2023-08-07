from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_browser = Chrome(service=Service(ChromeDriverManager().install()))

chrome_browser.quit()