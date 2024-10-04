import psutil
import logging

# Logging configuration
logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80  # in percent
MEMORY_THRESHOLD = 80  # in percent
DISK_THRESHOLD = 80  # in percent

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    else:
        logging.info(f"CPU usage is normal: {cpu_usage}%")

def check_memory():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {memory_usage}%")
    else:
        logging.info(f"Memory usage is normal: {memory_usage}%")

def check_disk():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"Low Disk Space: {disk_usage}% used")
    else:
        logging.info(f"Disk usage is normal: {disk_usage}%")

def check_processes():
    processes = [proc.info for proc in psutil.process_iter(['pid', 'name'])]
    logging.info(f"Number of running processes: {len(processes)}")

if __name__ == "__main__":
    check_cpu()
    check_memory()
    check_disk()
    check_processes()
