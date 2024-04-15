import psutil

def check_system_health():
  """
  This function checks system health by monitoring CPU usage, memory usage, disk space, and running processes.
  """
  cpu_threshold = 80
  mem_threshold = 80
  disk_threshold = 90
  process_threshold = 100  
  
  cpu_usage = psutil.cpu_percent(interval=1)
  mem_usage = psutil.virtual_memory().percent
  disk_usage = psutil.disk_usage('/').percent

  if cpu_usage > cpu_threshold:
    print(f"WARNING: CPU usage is at {cpu_usage}% (above threshold of {cpu_threshold}%)")

  if mem_usage > mem_threshold:
    print(f"WARNING: Memory usage is at {mem_usage}% (above threshold of {mem_threshold}%)")

  if disk_usage > disk_threshold:
    print(f"WARNING: Disk space usage is at {disk_usage}% (above threshold of {disk_threshold}%)")

  running_processes = len(list(psutil.process_iter()))
  if running_processes > process_threshold:
    print(f"WARNING: High number of running processes: {running_processes} (above threshold of {process_threshold})")


if __name__ == "__main__":
  check_system_health()
