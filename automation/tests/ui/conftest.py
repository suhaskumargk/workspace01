import pytest
from automation.utils.config_manager import ConfigManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import WebDriverException


@pytest.fixture(scope='session')
def driver(request):
	driver = None
	try:
		service = ChromeService(executable_path=ChromeDriverManager().install())
		driver = webdriver.Chrome(service=service)
		driver.maximize_window()
	except WebDriverException as e:
		print(f"Error occurred while initializing WebDriver (WebDriverException): {e}")
	yield driver
	driver.close()

