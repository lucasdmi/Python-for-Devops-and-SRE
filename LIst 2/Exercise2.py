import subprocess
output=subprocess.check_output('ps -ef | grep root', shell=True)
print(output)   


proc = subprocess.Popen(['ps -ef | grep root'], stdout=subprocess.PIPE)
output, err = proc.communicate()

if err:
    print(err)
else:
    # Split the output into lines
    lines = output.decode('utf-8').splitlines()

    # Sort the lines
    sorted_lines = sorted(lines, key=lambda line: line.split()[0])

    # Print the sorted lines
    for line in sorted_lines:
        print(line)