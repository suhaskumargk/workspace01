import pytest
import requests
import allure
from automation.utils.config_manager import ConfigManager

@allure.title("Prepare for the test")
@pytest.fixture(scope='session')
def api_config():
	cm = ConfigManager()
	return cm