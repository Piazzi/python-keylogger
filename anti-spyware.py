from win32com.client import GetObject
import subprocess
import os
import sys
print(sys.argv[0][:-3])

pid = str(os.getpid())
print("Spyware PID: " + pid)
 
# traverse the software list
Data = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
processes = str(Data)

#  arrange the string
def arrange_string(string):
    return string.split("\\r\\r\\n")

warning_count = 0
try:
    for i in range(len(processes)):
        process = arrange_string(processes)[i]
        if process.find("py") > 0 and process.find(pid) == -1:
            print("\n------------- WARNING ------------- ")
            warning_count += 1
        print(process)
        if(warning_count > 0):
             print("------------- WARNING ------------- \n")
        warning_count = 0

except IndexError as e:
    print("All Done")

