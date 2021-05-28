import requests
import json

# вызов API и сохранение ответа
url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# анализ структуры данных
response_dict = r.json()
readable_file = r"D:\study\project 2\data\readable_hn_data.json"
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)