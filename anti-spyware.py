import ctypes  # An included library with Python install.   

import subprocess

cmd = 'WMIC PROCESS get Caption,Commandline,Processid'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

def clean_data(line):
    return str(line).replace(' ', '')

print("-------------------- Running processes --------------------")
for line in proc.stdout:
    line = clean_data(line)
    if(str(line).find(".py") != -1):
        print('\n ------------ WARNING- -----------  \n'+line+'\n ------------ WARNING- ----------- \n')
        ctypes.windll.user32.MessageBoxW(0, "Someone may be trying to steal your data. Check the following file: \n"+line, "Warning!", 1)
    else:
        print(clean_data(line))

