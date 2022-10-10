import json
import requests


class TestRecipients:
    def test_recipients_flow(self):
        base_url = "http://0.0.0.0:8000/"
        recipients_path = "api/recipients"

        # Get recipients
        path = "api/recipients"
        response = requests.get(url=f"{base_url}{path}")
        assert response.status_code == 200

        # Create a recipient
        recipient_data = {
            "name": "Maria",
            "surname": "Doe",
            "vat_number": 54321,
            "age": 34
        }
        response = requests.post(url=f"{base_url}{recipients_path}", data=json.dumps(recipient_data))
        assert response.status_code == 200
        recipient_id = json.loads(response.text)["id"]

        # Delete a recipient
        response = requests.delete(url=f"{base_url}{recipients_path}/{recipient_id}", data=json.dumps(recipient_data))
        assert response.status_code == 200
