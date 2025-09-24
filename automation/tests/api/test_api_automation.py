import pytest
import requests
from automation.utils.common_methods import common_methods
from automation.utils.config_manager import ConfigManager
from . import api_helpers
import allure
import logging


logger = logging.getLogger(__name__)

class Test_API_Automation:

    @allure.title("Test create user")
    @allure.description("This test attempts to create a user in the system.")
    @allure.testcase("TESTCASE-001")
    @pytest.mark.api
    def test_post_create_user(self):
        base_url = ConfigManager.get('api_data', 'base_url')
        headers = common_methods.get_json_payload('headers.json')
        payload = common_methods.get_json_payload('create_user.json')
        username , password  = common_methods.get_credentials_from_xlsx('userdata.xlsx')
        response = api_helpers.post_create_user(base_url, headers, payload, username, password)
        assert response is True

    @allure.title("Test update user")
    @allure.description("This test attempts to update a user in the system.")
    @allure.testcase("TESTCASE-002")
    @pytest.mark.api
    def test_post_updateuser(self):
        base_url = ConfigManager.get('api_data', 'base_url')
        headers = common_methods.get_json_payload('headers.json')
        payload = common_methods.get_json_payload('create_user.json')
        response = api_helpers.post_create_single_user(base_url, headers, payload)
        assert response is not None
        payload = common_methods.get_json_payload('update_user.json')
        response = api_helpers.put_update_user(base_url, headers, payload, response)
        assert response is not None
        
    @allure.title("Test get users")
    @allure.description("This test attempts to retrieve a list of users from the system.")
    @allure.testcase("TESTCASE-003")
    @pytest.mark.api
    def test_get_users(self):
        base_url = ConfigManager.get('api_data', 'base_url')
        response = api_helpers.get_users(base_url)
        assert response is not None

    @allure.title("Test delete user")
    @allure.description("This test attempts to delete a user from the system.")
    @allure.testcase("TESTCASE-004")
    @pytest.mark.api
    def test_del_user(self):
        base_url = ConfigManager.get('api_data', 'base_url')
        headers = common_methods.get_json_payload('headers.json')
        payload = common_methods.get_json_payload('create_user.json')
        response = api_helpers.post_create_single_user(base_url, headers, payload)
        assert response is not None
        response = api_helpers.delete_user(base_url, headers, response)
        assert response is not None