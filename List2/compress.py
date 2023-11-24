import gzip
import shutil
import subprocess

with open('ola.txt', 'rb') as f, gzip.open('ola.txt.gz', 'wb') as z:
    shutil.copyfileobj(f, z)


output=subprocess.check_output('ls \n', shell=True)
print(output)

