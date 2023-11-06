from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)


def test_start_api_post():
    """
    Test Case Name: test_start_api_post
    Test Purpose: Verify if a certain one item works as expected by POST.
    Input Parameters: Set default_config's request_type in local_runner.py
    Expected Behavior: After calling this function, it is expected to return a specific result.
    """
    response = client.post("/api", json={"item": "province_count"})
    assert response.status_code == 200
    data = response.json()
    print(f'\n{data}')


def test_start_api_get():
    """
        Test Case Name: test_start_api_get
        Test Purpose: Verify if a certain one item works as expected by GET.
        Input Parameters: Set default_config's request_type in local_runner.py
        Expected Behavior: After calling this function, it is expected to return a specific result.
        """
    response = client.get(f"/api/province_count")
    assert response.status_code == 200
    data = response.json()
    print(f'\n{data}')
