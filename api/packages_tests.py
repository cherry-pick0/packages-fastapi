import json
import pytest
import requests


class TestPackages:

    def test_get_packages(self):
        path = "api/package"
        base_url = "http://0.0.0.0:8000/"
        response = requests.get(url=f"{base_url}{path}")
        responseJson = json.loads(response.text)
        assert response.status_code == 200
