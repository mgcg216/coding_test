import threading
import time

def delayed_print(x):
    print(x)
    for i in range(10):
        print(x, " ", i)
        time.sleep(.5)
x="TEST"
y="BESTSDFSDF"
t1 = threading.Thread(target=delayed_print, args=(x,))
t2 = threading.Thread(target=delayed_print, args=(y,))

for i in range(10):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!", i)
    t1.start()
    t2.start()
    t1.join()
    t2.join()