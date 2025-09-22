import allure
import pytest
from selenium import webdriver
import logging

logger = logging.getLogger(__name__)

@allure.title("Prepare for the test")
@pytest.fixture(scope="session")
def driver(request):
    driver = None
    driver = webdriver.Chrome()
    driver.maximize_window()
    logger.info("STARTING THE CHROME BROWSER FOR TEST")
    yield driver
    logger.info("TEST COMPLETED, CLOSING THE BROWSER.")
    driver.close()
