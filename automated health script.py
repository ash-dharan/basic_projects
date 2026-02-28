import os
import datetime
import psutil
import platform
import socket

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
log_file = os.path.join(log_dir, f"report_{timestamp}.txt")

with open(log_file, "w") as f:
    f.write("===== SYSTEM HEALTH REPORT =====\n")
    f.write(f"Generated on: {timestamp}\n")
    f.write(f"Hostname: {socket.gethostname()}\n")
    f.write(f"OS: {platform.system()} {platform.release()}\n\n")

    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = now - boot_time
    f.write(f"--- Uptime ---\nBoot Time: {boot_time}\nUptime: {str(uptime).split('.')[0]}\n\n")

    f.write("--- CPU Info ---\n")
    f.write(f"Physical cores: {psutil.cpu_count(logical=False)}\n")
    f.write(f"Total cores: {psutil.cpu_count(logical=True)}\n")
    f.write(f"CPU usage per core: {psutil.cpu_percent(percpu=True)}\n")
    f.write(f"Total CPU usage: {psutil.cpu_percent()}%\n\n")

    mem = psutil.virtual_memory()
    f.write("--- Memory Info ---\n")
    f.write(f"Total: {mem.total / (1024**3):.2f} GB\n")
    f.write(f"Available: {mem.available / (1024**3):.2f} GB\n")
    f.write(f"Used: {mem.used / (1024**3):.2f} GB\n")
    f.write(f"Percentage: {mem.percent}%\n\n")

    # f.write("--- Disk Info ---\n")
    # partitions = psutil.disk_partitions()
    # for p in partitions:
    #     f.write(f"Mountpoint: {p.mountpoint}, Filesystem: {p.fstype}\n")
    #     usage = psutil.disk_usage(p.mountpoint)
    #     f.write(f"  Total: {usage.total / (1024**3):.2f} GB\n")
    #     f.write(f"  Used: {usage.used / (1024**3):.2f} GB\n")
    #     f.write(f"  Free: {usage.free / (1024**3):.2f} GB\n")
    #     f.write(f"  Percentage: {usage.percent}%\n")
    # f.write("\n")

    f.write("--- Network Info ---\n")
    net_io = psutil.net_io_counters()
    f.write(f"Bytes Sent: {net_io.bytes_sent / (1024**2):.2f} MB\n")
    f.write(f"Bytes Received: {net_io.bytes_recv / (1024**2):.2f} MB\n\n")

    f.write("--- Top 5 Processes (by CPU) ---\n")
    processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']), key=lambda p: p.info['cpu_percent'], reverse=True)
    for p in processes[:5]:
        f.write(f"PID: {p.info['pid']}, Name: {p.info['name']}, CPU: {p.info['cpu_percent']}%\n")

print(f"Report generated: {log_file}")