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

    @pytest.mark.api
    def test_post_updateuser(self, api_config):
        base_url = api_config.get('api_data', 'base_url')
        headers = common_methods.get_json_payload('headers.json')
        payload = common_methods.get_json_payload('update_user.json')
        response = requests.put(f"{base_url}/users/1", json=payload, headers=headers)
        assert response.status_code == 200
        assert response.json()
        logger.info(response.json())

    @pytest.mark.api
    def test_get_users(self, api_config):
        base_url = api_config.get('api_data', 'base_url')
        response = requests.get(f"{base_url}/users")
        assert response.status_code == 200
        assert response.json()
        logger.info(response.json())

    @pytest.mark.api
    def test_del_user(self, api_config):
        base_url = api_config.get('api_data', 'base_url')
        headers = common_methods.get_json_payload('headers.json')
        response = requests.delete(f"{base_url}/users/1", headers=headers)
        assert response.status_code == 200
        assert response.json()
        logger.info(response.json())
    