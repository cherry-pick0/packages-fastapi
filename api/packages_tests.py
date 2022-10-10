import json
import requests


class TestPackages:
    def test_packages_flow(self):
        base_url = "http://0.0.0.0:8000/"
        recipients_path = "api/recipients"
        packages_path = "api/packages"

        # Get packages
        path = "api/packages"
        response = requests.get(url=f"{base_url}{path}")
        assert response.status_code == 200

        # Create a package
        recipient_data = {
            "name": "Maria",
            "surname": "Doe",
            "vat_number": 54321,
            "age": 34
        }
        response = requests.post(url=f"{base_url}{recipients_path}", data=json.dumps(recipient_data))
        assert response.status_code == 200
        recipient_id = json.loads(response.text)["id"]

        package_data = {
            "address": "Fake address234",
            "weight": 20,
            "recipient_id": recipient_id
        }
        response = requests.post(url=f"{base_url}{packages_path}", data=json.dumps(package_data))
        assert response.status_code == 200
        package_id = json.loads(response.text)["id"]

        # Delete a package
        response = requests.delete(url=f"{base_url}{packages_path}/{package_id}", data=json.dumps(recipient_data))
        assert response.status_code == 200
