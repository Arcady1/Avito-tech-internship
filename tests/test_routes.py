from server.app import app
import json


def test_get_balance():
    response = app.test_client().get("http://127.0.0.1:8080/api/v1.0/balance/users?user_id=122")
    resp = json.loads(response.data)
    print(resp["data"])
    assert response.status_code == 200
