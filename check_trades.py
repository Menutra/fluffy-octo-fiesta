import requests
import json
import os

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
PUSHOVER_TOKEN = os.getenv('PUSHOVER_TOKEN')
PUSHOVER_USER_KEY = os.getenv('PUSHOVER_USER_KEY')

def check_trades():
    url = "https://tradeogre.com/api/v1/account/orders"
    headers = {
        "Authorization": f"Bearer {API_KEY}:{API_SECRET}"
    }
    response = requests.get(url, headers=headers)
    trades = json.loads(response.text)

    for trade in trades:
        if trade['status'] == 'completed':
            send_notification(trade)

def send_notification(trade):
    message = f"Trade {trade['id']} for {trade['amount']} {trade['market']} has been completed."
    requests.post("https://api.pushover.net/1/messages.json", data={
        "token": PUSHOVER_TOKEN,
        "user": PUSHOVER_USER_KEY,
        "message": message
    })

if __name__ == "__main__":
    check_trades()
