import pytest
import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def chrome_browser():
    options = Options()
    options.add_argument("--disable-extensions")
    # options.add_argument("--headless")
    driver = selenium.webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def chrome_joom():
    driver = Chrome()
    driver.get("https://joom.com/en")
    yield driver
    driver
