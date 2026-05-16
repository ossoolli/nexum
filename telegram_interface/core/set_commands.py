import requests
import os

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
url = f'https://api.telegram.org/bot{TOKEN}/setMyCommands'
commands = {
    'commands': [
        {'command': 'dashboard', 'description': 'لوحة التحكم الرئيسية'},
        {'command': 'fix_all', 'description': 'إصلاح شامل للنظام'},
        {'command': 'status', 'description': 'حالة النظام'}
    ]
}
requests.post(url, json=commands)
