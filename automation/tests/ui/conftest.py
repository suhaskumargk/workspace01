
import pytest
from automation.utils.config_manager import ConfigManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

import allure


@allure.title("Prepare for the test")
@pytest.fixture(scope='session')
def driver(request):
	config = ConfigManager()
	browser = (config.get('settings', 'browser') or 'chrome').strip().lower()
	driver = None
	try:
		if browser == 'chrome':
			service = ChromeService(executable_path=ChromeDriverManager().install())
			driver = webdriver.Chrome(service=service)
		elif browser in ('firefox', 'ff'):
			service = FirefoxService(executable_path=GeckoDriverManager().install())
			driver = webdriver.Firefox(service=service)
		elif browser in ('edge', 'msedge'):
			service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
			driver = webdriver.Edge(service=service)
		else:
			service = ChromeService(executable_path=ChromeDriverManager().install())
			driver = webdriver.Chrome(service=service)
		if driver:
			driver.maximize_window()
	except WebDriverException as e:
		print(f"Error occurred while initializing WebDriver (WebDriverException): {e}")
	yield driver
	driver.close()

