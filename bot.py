import json
import requests

webhook_url = 'https://discord.com/api/v9/channels/1066043579807572038/messages'
message = 'hejlou'

payload = {'content': message}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'MTA0MTA0ODk5MTAzMjQyNjU5OA.GBbYXP.kpxQYfWXrqgH1hjg0Rq6x7YdkXLEUJi0tt7eQA'
}

response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
print(response.status_code)