# Single Prompt
import requests
import json

response = requests.post(
    'https://bing.khanh.lol/completion',
    headers={'Content-Type': 'application/json'},
    data=json.dumps({'prompt': 'Hello, World!'})
)

print(response.text)

data = response.json()
print(data['response'])
# Output:
# Hello, user! I'm Sydney, your AI assistant. I'm here to help you with anything you need. 😊