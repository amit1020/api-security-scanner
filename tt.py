import requests

a = requests.post("http://127.0.0.1:8000/", data={"target_url": "https://www.python.org"})

if a.status_code == 200:
    print("Scan started successfully!")
    print(a.text)
else:
    print("Failed to start scan!")