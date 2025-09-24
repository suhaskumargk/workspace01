import requests
import logging

logger = logging.getLogger(__name__)

def post_create_user(base_url, headers, payload, username, password):
    """Sends a POST request to a specified endpoint."""
    res = False
    for i in range(15):
        payload['username'] = username[i]
        payload['password'] = password[i]
        logger.info(f"Creating user: {username[i]} with password: {password[i]}")
        response = requests.post(f'{base_url}/users/add', json=payload, headers=headers)
        assert response.status_code == 201
        logger.info(f"Response Status Code: {response.status_code}")
        assert response.json().get('id') is not None
        logger.info("New User created")
        res = True
    return res
    
def post_create_single_user(base_url, headers, payload):
    """Sends a POST request with data to a specified endpoint."""
    logger.info("creating user for validate update")
    response = requests.post(f'{base_url}/users/add', json=payload, headers=headers)
    assert response.status_code == 201
    logger.info(f"Response Status Code: {response.status_code}")
    assert response.json().get('id') is not None
    logger.info("New User created")
    return response.json()

def put_update_user(base_url, headers, payload, previous_response):
    """Sends a PUT request with data to a specified endpoint."""
    logger.info("updating user")
    response = requests.put(f"{base_url}/users/{(previous_response.get('id'))-1}", json=payload, headers=headers)
    logger.info(f"Response Status Code: {response.status_code}")
    assert response.status_code == 200
    logger.info("Updated a User")
    assert response.json()
    return response.json()

def get_users(base_url):
    """Sends a GET request to a specified endpoint."""
    logger.info("getting list of users")
    response = requests.get(f"{base_url}/users")
    logger.info(f"Response Status Code: {response.status_code}")
    assert response.status_code == 200
    assert response.json()
    return response.json()

def delete_user(base_url, headers, previous_response):
    """Sends a DELETE request to a specified endpoint."""
    logger.info("deleting user")
    response = requests.delete(f"{base_url}/users/{(previous_response.get('id'))-1}", headers=headers)
    logger.info(f"Response Status Code: {response.status_code}")
    assert response.status_code == 200
    logger.info("Deleted a User")
    assert response.json()
    return response.json()
