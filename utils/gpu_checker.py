from pynvml import (
    nvmlInit,
    nvmlShutdown,
    nvmlDeviceGetCount,
    nvmlDeviceGetHandleByIndex,
    nvmlDeviceGetName,
    nvmlDeviceGetMemoryInfo,
    nvmlDeviceGetUtilizationRates,
    nvmlDeviceGetTemperature,
    NVML_TEMPERATURE_GPU
)
import csv
import os
import time

def check_gpu(config):
    nvmlInit()
    alerts = []
    summary_lines = []

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    log_dir = os.path.dirname(config["log_file"])
    os.makedirs(log_dir, exist_ok=True)

    if not os.path.exists(config["log_file"]):
        with open(config["log_file"], "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Time", "GPU", "Temp (°C)", "Util (%)", "Memory Used (MB)", "Total Memory (MB)"])

    for i in range(nvmlDeviceGetCount()):
        handle = nvmlDeviceGetHandleByIndex(i)
        name = nvmlDeviceGetName(handle)
        if isinstance(name, bytes):
            name = name.decode()
        temp = nvmlDeviceGetTemperature(handle, NVML_TEMPERATURE_GPU)
        util = nvmlDeviceGetUtilizationRates(handle).gpu
        mem_info = nvmlDeviceGetMemoryInfo(handle)
        used_mb = mem_info.used / 1024 ** 2
        total_mb = mem_info.total / 1024 ** 2

        # Log to CSV
        with open(config["log_file"], "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, name, temp, util, f"{used_mb:.1f}", f"{total_mb:.1f}"])

        if temp > config["warning_temperature"]:
            alerts.append(f"[{timestamp}] ALERT: {name} temp is {temp}°C (threshold {config['warning_temperature']}°C)")

        if util > config["warning_utilization"]:
            alerts.append(f"[{timestamp}] ALERT: {name} utilization is {util}% (threshold {config['warning_utilization']}%)")

        summary_lines.append(f"{name}: Temp={temp}°C, Util={util}%, Mem={used_mb:.1f}/{total_mb:.1f} MB")

    # nvmlShutdown()
    # return alerts, summary_lines
