import json
from datetime import datetime, timezone
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(API_URL, timeout=20)
if response.status_code != 200:
    print(f"Request failed with status code: {response.status_code}")
    exit(1)

print("status:", response.status_code)
print("content-type:", response.headers.get("Content-Type"))

payload = response.json()
print("top-level type:", type(payload).__name__)

with open("data/raw/api_snapshot.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)

print("retrieved_at_utc:", datetime.now(timezone.utc).isoformat())
print("number of records:", len(payload))
print("sample record:", payload[0] if payload else "No records found")