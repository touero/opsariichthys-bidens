import requests

url = 'http://127.0.0.1:2518/api'  # 请将URL更改为您的FastAPI服务器地址
data = {"item": "province_count"}  # 根据您的数据结构提供正确的数据

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Error: {response.status_code}")
