# synchronization Example
# First step is LOCKING

import threading
import time

x = 8192
lock = threading.Lock()

def double():
    global x, local
    lock.acquire()

    while x < 16384:
        x *=2
        print(x)
        time.sleep(1)
    print("Reached the maximum!")
    lock.release()

def halve():
    global x,local
    lock.acquire()
    while x > 1:
        x /=2
        print(x)
        time.sleep(1)
    print("Reached the minimum!")
    lock.release()

# Threads to execute 
t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

t1.start()
t2.start()

