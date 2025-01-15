# Task 2: Backing Up a Configuration File
import shutil

try:
    # Back up the configuration file
    shutil.copy("nginx.conf", "nginx.conf.bak")
    print("Backup created: nginx.conf.bak")
except FileNotFoundError:
    print("Configuration file not found.")
except PermissionError:
    print("Permission denied while creating the backup.")