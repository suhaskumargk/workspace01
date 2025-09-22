import allure
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
import logging

logger = logging.getLogger(__name__)

@allure.title("Prepare for the test")
@pytest.fixture(scope="session")
def driver(request):
    driver = None
    path = ChromeDriverManager().install()
    service = ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    logger.info("STARTING THE CHROME BROWSER FOR TEST")
    yield driver
    logger.info("TEST COMPLETED, CLOSING THE BROWSER.")
    driver.close()
