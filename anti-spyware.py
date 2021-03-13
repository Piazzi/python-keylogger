from win32com.client import GetObject
import subprocess
import os
import sys
import win32api

print(sys.argv[0][:-3])
pid = str(os.getpid())
print("Anti Spyware PID: " + pid+ "\n")
 
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
            win32api.MessageBox(0, 'The following processes may be a spyware: \nHandle Name Priority ProcessId ThreadCount WorkingSetSize\n'+process , 'Warning!')
            print("\n------------- WARNING ------------- ")
            warning_count += 1
        print(process)
        if(warning_count > 0):
             print("------------- WARNING ------------- \n")
        warning_count = 0

except IndexError as e:
    print("All Done")

