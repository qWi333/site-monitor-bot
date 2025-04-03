import requests
import time
import telebot

# === НАСТРОЙКИ ===
TELEGRAM_TOKEN = '7871404832:AAEqAB8OQU-xbRd4Tn_8iE3NsycFnIXaNOQ'      # Пример: '123456789:ABCdefGhIjKlmNoPQRstuVWXyz'
TELEGRAM_CHAT_ID = '-4774165897'       # Пример: '123456789'
URL_TO_CHECK = 'https://victifin.org/' # Сайт для проверки
CHECK_INTERVAL = 60                    # Время между проверками (в секундах)

# === НЕ ИЗМЕНЯЙТЕ НИЖЕ ЭТОЙ СТРОКИ ===
bot = telebot.TeleBot(TELEGRAM_TOKEN)
was_offline = True  # Предполагаем, что сайт изначально недоступен

while True:
    try:
        response = requests.get(URL_TO_CHECK, timeout=10)
        if response.status_code == 200:
            if was_offline:
                message = f"✅ Сайт {URL_TO_CHECK} снова доступен!"
                bot.send_message(TELEGRAM_CHAT_ID, message)
                was_offline = False
        else:
            was_offline = True
    except Exception as e:
        was_offline = True
    time.sleep(CHECK_INTERVAL)
