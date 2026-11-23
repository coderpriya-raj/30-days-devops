import sys
from pathlib import Path
import psutil
import json


def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage


def get_memory_usage():
    memory_usage = psutil.virtual_memory().percent
    return memory_usage


def get_disk_usage():
    disk_usage = psutil.disk_usage("/").percent
    return disk_usage



def check_threshold(usage, limit, resource_name):
    if usage > limit:
        print(f"WARNING: High {resource_name} usage detected!")
        return False
    else:
        print(f"{resource_name} usage is normal.")
        return True



cpu = get_cpu_usage()
print(f"CPU usage: {cpu}%")


memory = get_memory_usage()
print(f"Memory usage: {memory}%")


disk = get_disk_usage()
print(f"Disk Usage: {disk}%")


cpu_status = check_threshold(cpu, 80, "CPU")
memory_status = check_threshold(memory, 85, "Memory")
disk_status = check_threshold(disk, 90, "Disk")

if cpu_status and memory_status and disk_status :
    system_status = "HEALTHY"
else:
    system_status = "UNHEALTHY"
print(f"SYSTEM STATUS: {system_status}")


report = {
    "cpu_usage": cpu,
    "memory_usage": memory,
    "disk_usage": disk,
    "system_status": system_status
}

json_report = json.dumps(report, indent=4)
print(json_report)

report_folder = Path("reports")
report_folder.mkdir(parents=True, exist_ok=True)
with open("reports/health_report.json", "w") as file:
    file.write(json_report)

if system_status == "HEALTHY":
    sys.exit(0)
else:
    sys.exit(1)