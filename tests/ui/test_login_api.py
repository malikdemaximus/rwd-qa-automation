import requests

def test_valid_login():
    data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post("https://reqres.in/api/login", data=data)
    assert response.status_code == 200
    assert "token" in response.json()

def test_invalid_login():
    data = {"email": "eve.holt@reqres.in"}
    response = requests.post("https://reqres.in/api/login", data=data)
    assert response.status_code == 400
