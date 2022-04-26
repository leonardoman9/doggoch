import requests
import IDs

def send_photo(chat_id, file_opened):
    method = "sendPhoto"
    params = {'chat_id': chat_id}
    files = {'photo': file_opened}
    resp = requests.post('https://api.telegram.org/bot' + IDs.TELEGRAM_BOT_TOKEN + '/sendPhoto', params, files=files)
    return resp