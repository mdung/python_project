import requests

data = {'cpu_usage': 75, 'ram_usage': 90, 'storage_usage': 220, 'transaction_count': 220}
response = requests.post('http://localhost:5000/get_recommendation', json=data)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
