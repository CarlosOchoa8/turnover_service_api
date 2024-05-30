from tests.conftest import client
from tests.endpoints.mocks import (collaborator_data, collaborator_id,
                                   collaborator_id_fake)


def test_post_method():
    """
    Test the POST method for creating a new collaborator.
    Returns: collaborator object stored in db
    """
    response = client.post(
        "api/v1/collaborators/", json=collaborator_data)

    assert response.status_code == 200
    assert '"employee_number":12345' in response.text


def test_get_method():
    """
    Test the POST method for creating a new collaborator.
    Returns: collaborator object stored in db
    """
    response = client.get(
        f"api/v1/collaborators/score/{collaborator_id}")
    assert response.status_code == 200
    assert '"employee_number":12345' in response.text


def test_existent_collaborator_in_post_method():
    """
    Test the POST method for creating a new collaborator.
    Returns: collaborator object stored in db
    """
    response = client.post(
        "api/v1/collaborators/", json=collaborator_data)
    assert response.status_code == 200
    assert '{"message":"Collaborator 12345 is already registered.","collaborator id":12345,"collaborator score":0.3249136199461228}' in response.text


def test_not_collaborator_retrieved_from_get_method():
    """
    Test the POST method for creating a new collaborator.
    Returns: collaborator object stored in db
    """
    response = client.get(
        f"api/v1/collaborators/score/{collaborator_id_fake}")

    assert response.status_code == 404
    assert f'Collaborator {collaborator_id_fake} does not have record.' in response.text
