import pyfirmata
import time


print("Loading Settings")
board = pyfirmata.ArduinoNano('COM9')
it = pyfirmata.util.Iterator(board)
it.start()

laser = board.get_pin('d:11:o')
dirx = board.get_pin('d:5:o')
diry = board.get_pin('d:6:o')
stepx = board.get_pin('d:2:o')
stepy = board.get_pin('d:3:o')

"""
laser = board.get_pin('d:11:o')
dirx = board.get_pin('d:5:o')
diry = board.get_pin('d:6:o')
stepx = board.get_pin('d:2:o')
stepy = board.get_pin('d:3:o')


while True:
    # laser.write(1)
    waitTime = 0
    dirx.write(1)
    print("Setting Clockwise")
    for i in range(2000):
        stepx.write(1)
        time.sleep(waitTime)
        stepx.write(0)
        time.sleep(waitTime)
        print(i, " Step X")
    # laser.write(0)
    time.sleep(1)

    # laser.write(1)
    dirx.write(0)
    print("Setting Counter-Clockwise")

    for i in range(2000):
        stepx.write(1)
        time.sleep(waitTime)
        stepx.write(0)
        time.sleep(waitTime)
        print(i, " Step X")
    # laser.write(0)
    time.sleep(1)

    diry.write(1)
    print("Setting Clockwise")
    # laser.write(1)
    for i in range(2000):
        stepy.write(1)
        time.sleep(waitTime)
        stepy.write(0)
        time.sleep(waitTime)
        print(i, " Step Y")
    # laser.write(0)
    time.sleep(1)

    diry.write(0)
    print("Setting Counter-Clockwise")
    # laser.write(1)
    for i in range(2000):
        stepy.write(1)
        time.sleep(waitTime)
        stepy.write(0)
        time.sleep(waitTime)
        print(i, " Step Y")
    # laser.write(0)
    time.sleep(1)
"""
