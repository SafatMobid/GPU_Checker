GPU Health Monitor & Alert System
+++++ FOR NVIDIA GPU ONLY +++++

Personal Python Project created to monitor my system GPU Temp and Usage. Should send email alerts if the temperature exceeds a certain amount and logs data to a CSV file for tracking.
- Useful to proactively monitor PC hardware

Library Used:
csv
os
time
pynvml (for Nvidia GPU)

for email capabilites:
json
schedule
time
smtplib

+++++ Alert Example Email+++++
Subject: GPU Alert: High Temperature
Body:

GPU: NVIDIA RTX 3070
Temperature: 83°C
Memory Usage: 85.6%
Time: 2025-05-18 10:37:45


TO BE ADDED:
- Start on Windows StartUp
- Support for CPU and RAM monitoring
- Text Alerts
- Cleaner CSV File
