import os, sqlite3, subprocess, psutil, requests, json, time
from datetime import datetime

TELEGRAM_BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = "625341234"

def send_sovereign_alert(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})

def active_defense(ip):
    subprocess.run(f"sudo iptables -A INPUT -s {ip} -j DROP", shell=True)
    send_sovereign_alert(f"🚨 *دفاع نشط:* تم حظر الـ IP المشبوه {ip} تلقائياً.")

def sysadmin_monitor():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    if cpu > 80 or ram > 80:
        send_sovereign_alert(f"⚠️ *تنبيه موارد:* استهلاك المعالج {cpu}% والذاكرة {ram}%.")

def main_loop():
    print("🚀 المحرك المتكامل انطلق...")
    while True:
        sysadmin_monitor()
        time.sleep(300)

if __name__ == "__main__":
    main_loop()
