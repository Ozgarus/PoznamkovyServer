import json
import requests

webhook_url = 'https://discord.com/api/v9/channels/1066043579807572038/messages'
message = 'hejlou'

payload = {'content': message}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'token'
}

response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
print(response.status_code)