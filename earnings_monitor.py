import os
import requests

webhook = os.environ["DISCORD_WEBHOOK"]

message = {
    "content": "GitHub Actionsからテスト通知"
}

response = requests.post(
    webhook,
    json=message
)

print(response.status_code)
