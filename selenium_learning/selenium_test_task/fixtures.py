import pytest
import selenium
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def chrome_browser():
    options = Options()
    # options.add_argument("--headless")
    driver = selenium.webdriver.Chrome(options=options)
    yield driver
    driver.quit()