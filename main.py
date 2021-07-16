import requests
import sys


# Script for posting events in Telegram

BOT_TOKEN = 'FILL'
BOT_CHAT_ID = sys.argv[1]
RULE_NAME = sys.argv[2]
SOURCE_IP = sys.argv[3]
SOURCE_PORT = sys.argv[4]
DESCTINATION_IP = sys.argv[5]
DESCTINATION_PORT = sys.argv[6]
QID = sys.argv[7]
EVENT_NAME = sys.argv[8]
CATEGORY = sys.argv[9]
LOG_SOURCE = sys.argv[10]
PAYLOAD = sys.argv[11]

PROXIES = {
 'http': 'http://proxy.sactech.dev:3128',
 'https': 'http://proxy.sactech.dev:3128'
}


def post_telegram_issue(message):
    send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + BOT_CHAT_ID + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text, proxies=PROXIES, verify=False)
    return response.json()


if __name__ == '__main__':
    telegram_issue = 'Rule name: {title}\r\nSource IP: {source_ip}\r\nSource port: {source_port}\r\nDestination IP: {destination_ip}\r\nDestination port: {destination_port}\r\nQID: {qid}\r\nEvent: {event}\r\nCategory: {category}\r\nLog source: {log_source}\r\nPayload: {payload}'.format(
        title=RULE_NAME, source_ip=SOURCE_IP, source_port=SOURCE_PORT, destination_ip=DESCTINATION_IP,
        destination_port=DESCTINATION_PORT, qid=QID, event=EVENT_NAME, category=CATEGORY, log_source=LOG_SOURCE,
        payload=PAYLOAD)

    post_telegram_issue(telegram_issue)
