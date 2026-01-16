import schedule
import time
from whatsapp import send_message
from config import *

print("🟢 Scheduler iniciado, aguardando horário...")

def job():
    send_message(WHATSAPP_NUMBER, MESSAGE, CHROME_PROFILE_PATH)

schedule.every().day.at(f"{SEND_HOUR:02d}:{SEND_MINUTE:02d}").do(job)

while True:
    schedule.run_pending()
    time.sleep(30)
