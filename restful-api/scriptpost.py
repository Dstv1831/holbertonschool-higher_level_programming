import requests

url = "http://127.0.0.1:5000/login"
data = {"username": "David", "password": "abc123"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.json())  # Should return a JWT token if successful