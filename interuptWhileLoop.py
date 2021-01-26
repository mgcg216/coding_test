# import time,threading
#
# class example(threading.Thread):
#
#     def __init__(self):
#         threading.Thread.__init__(self,target=self.run)
#
#         self.__recording = False
#
#     def run(self):
#         self.__recording = True
#         while self.__recording:
#             time.sleep(1)
#             print(1)
#
#     def join(self):
#         self.__recording = False
#         threading.Thread.join(self)
#
# a = example()
# a.start()
# time.sleep(5)
# a.join()

import time,threading

class example():

    def __init__(self):
        self.__recording = False

    def asdf(self):
        self.__recording = True
        while self.__recording:
            time.sleep(1)
            print(1)

    def stop(self):
        self.__recording = False

a = example()
t = threading.Thread(target=a.asdf)
t.start()
time.sleep(5)
a.stop()
t.join()


