# import threading
# import time
#
# def loop1_10():
#     for i in range(1, 11):
#         time.sleep(1)
#         print(i)
#
# threading.Thread(target=loop1_10).start()

import threading
import time


# class MyThread(threading.Thread):
#     def run(self):
#         print("{} started!".format(self.getName()))              # "Thread-x started!"
#         time.sleep(1)                                      # Pretend to work for a second
#         print("{} finished!".format(self.getName()))             # "Thread-x finished!"
# def main():
#     for x in range(4):                                     # Four times...
#         mythread = MyThread(name = "Thread-{}".format(x + 1))  # ...Instantiate a thread and pass a unique ID to it
#         mythread.start()                                   # ...Start the thread, invoke the run method
#         time.sleep(.9)                                     # ...Wait 0.9 seconds before starting another
# if __name__ == '__main__':main()

# from multiprocessing import Process
#
# def instruction():
#     print(1)
#     print(2)
#     print(4)
#     print(5)
#     print(4)
#     print(4)
#     print(6)
#
# def loopytest():
#     print("break")
#     print("break")
#     print("break")
#     print("break")
#     print("break")
#
# if __name__ == '__main__':
#     # threading.Thread(target=instruction()).start()
#     # threading.Thread(target=loopytest()).start()
#
#     p1 = Process(target=instruction)
#     p1.start()
#     p2 = Process(target=loopytest)
#     p2.start()
#     p1.join()
#     p2.join()

# !!!THREAD VS
from multiprocessing import Process
from threading import Thread

def func1():
  print('func1: starting')
  for i in range(1000000):
      print(i * 2-1)
  print('func1: finishing')

def func2():
  print('func2: starting')
  for i in range(100000):
      print(i*2)
  print('func2: finishing')

def func3():
    while True:
        print("hello")

def func4():
    print('func4: starting')
    for i in range(100000):
        print("hello")
    print('func4: finishing')


def runInParallelThread(*fns):
    proc = []
    for fn in fns:
        p = Thread(target=fn)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()

# if __name__ == '__main__':
#   p1 = Process(target=func1)
#   p1.start()
#   p2 = Process(target=func3)
#   p2.start()
#   p1.join()
#   p2.join()

if __name__ == '__main__':
    runInParallelThread(func1(),func3())
