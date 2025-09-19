import pytest
import requests
from automation.utils.common_methods import common_methods
import allure
import json
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Test_API_Automation:

    @allure.title("Test create user")
    @allure.description("This test attempts to create a user in the system.")
    @allure.testcase("TESTCASE-000")
    @pytest.mark.api
    def test_post_login_user(self, api_config):
        base_url = api_config.get('api_data', 'base_url')
        headers = common_methods.get_json_payload('headers.json')
        payload = common_methods.get_json_payload('create_user.json')
        response = requests.post(f'{base_url}/auth/login', json=payload, headers=headers)
        assert response.status_code == 200
        assert response.json().get('accessToken') is not None
        logger.info(response.json())

    @allure.title("Test create user")
    @allure.description("This test attempts to create a user in the system.")
    @allure.testcase("TESTCASE-001")
    @pytest.mark.api
    def test_post_create_user(self, api_config):
        base_url = api_config.get('api_data', 'base_url')
        headers = common_methods.get_json_payload('headers.json')
        payload = common_methods.get_json_payload('create_user.json')
        username , password  = common_methods.get_credentials_from_xlsx('userdata.xlsx')
        for i in range(15):
            payload['username'] = username[i]
            payload['password'] = password[i]
            response = requests.post(f'{base_url}/users/add', json=payload, headers=headers)
            assert response.status_code == 201
            assert response.json()
        logger.info(response.json())

    @allure.title("Test update user")
    @allure.description("This test attempts to update a user in the system.")
    @allure.testcase("TESTCASE-002")
    @pytest.mark.api
    def test_post_updateuser(self, api_config):
        base_url = api_config.get('api_data', 'base_url')
        headers = common_methods.get_json_payload('headers.json')
        payload = common_methods.get_json_payload('update_user.json')
        response = requests.put(f"{base_url}/users/208", json=payload, headers=headers)
        assert response.status_code == 200
        assert response.json()
        logger.info(response.json())

    @allure.title("Test get users")
    @allure.description("This test attempts to retrieve a list of users from the system.")
    @allure.testcase("TESTCASE-003")
    @pytest.mark.api
    def test_get_users(self, api_config):
        base_url = api_config.get('api_data', 'base_url')
        response = requests.get(f"{base_url}/users")
        assert response.status_code == 200
        assert response.json()
        logger.info(response.json())

    @allure.title("Test delete user")
    @allure.description("This test attempts to delete a user from the system.")
    @allure.testcase("TESTCASE-004")
    @pytest.mark.api
    def test_del_user(self, api_config):
        base_url = api_config.get('api_data', 'base_url')
        headers = common_methods.get_json_payload('headers.json')
        response = requests.delete(f"{base_url}/users/1", headers=headers)
        assert response.status_code == 200
        assert response.json()
        logger.info(response.json())
    