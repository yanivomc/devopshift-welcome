import subprocess
try:
    p = subprocess.run(["ls", "/var/log"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except FileNotFoundError:
    print("the command does not exist")
except PermissionError:
    print("do not have permission to run the process")
err = p.stderr.decode()
out = p.stdout.decode()
if "No such file or directory" in err:
    print("No such file or directory")
if "permission" in err:
    print("permission dined")
if p.returncode == 0:
    print(out)
    
    
p = subprocess.run(["systemctl", "status", "nginx"], stdout=subprocess.PIPE)
if "inactive" in p.stdout.decode():
    p = subprocess.run(["systemctl", "restart", "nginx"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(p.returncode)
    if p.returncode == 0:
        print("restart successful")
    else:
        print("restart failed")

