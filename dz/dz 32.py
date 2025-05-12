import requests
import json
import csv
req = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(req.text)
print(todos)

with open("dz32.csv", "w") as f:
    writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=todos[0].keys())
    writer.writeheader()
    for d in todos:
        writer.writerow(d)