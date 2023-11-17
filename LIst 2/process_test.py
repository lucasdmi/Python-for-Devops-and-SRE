import subprocess
output=subprocess.check_output('docker ps -a', shell=True)
print(output)
insert = subprocess.check_output('docker start sample-app', shell=True)
output=subprocess.check_output('docker ps ', shell=True)
print(output)

