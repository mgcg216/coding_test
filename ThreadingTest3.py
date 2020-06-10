# Python program showing
# how to kill threads
# using set/reset stop
# flag

import threading
import time


def run():
    while True:
        print('thread running')
        global stop_threads
        if stop_threads:
            break


stop_threads = False
t1 = threading.Thread(target=run)
t1.start()
time.sleep(1)
stop_threads = True
t1.join()
print('thread killed')

"""
import threading as th
import time

# global booly
# booly = False

def waiter():
    time.sleep(5)
    booly = True
    return booly


# th.Thread(target=waiter).start()

def checker():
    while True:
        print("Waiting")
        global booly
        if booly:
            break
    print("done")
# waiter()

# print(booly)

two = th.Thread(target=checker)
booly = False
one = th.Thread(target=waiter)

one.daemon = True
one.start()
two.daemon = True
two.start()
one.join()
two.join()
"""