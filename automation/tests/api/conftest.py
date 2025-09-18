import pytest
import requests
from automation.utils.config_manager import ConfigManager


@pytest.fixture(scope='session')
def api_config():
	cm = ConfigManager()
	return cm