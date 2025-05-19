import json
import schedule
import time
from utils.gpu_checker import check_gpu
from utils.notifier import send_email_alert

with open("config.json") as f:
    config = json.load(f)

def monitor():
    alerts, summary = check_gpu(config)
    if alerts:
        send_email_alert(alerts, config["email_settings"])

schedule.every(config["check_interval_minutes"]).minutes.do(monitor)

if __name__ == "__main__":
    print("GPU Monitor is running...")
    monitor()  # Run once immediately
    while True:
        schedule.run_pending()
        time.sleep(1)
