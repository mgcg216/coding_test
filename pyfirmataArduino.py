import pyfirmata
import time
import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
GPIO_PORT = "COM6"

for p in ports:
    if "Arduino" in p.description:
        GPIO_PORT = str(p[0])
    # print(p)
# Arduino GPIO setup
board = pyfirmata.ArduinoMega(GPIO_PORT)  # I cannot read with ArduinoNano possibly due to the old hardware
it = pyfirmata.util.Iterator(board)
it.start()

enable = board.get_pin("d:22:o")  # Head Suction Solenoid
suction = board.get_pin("d:48:o")  # Head Suction Solenoid
sol2 = board.get_pin("d:49:o")  # Solenoid 2 Plastic
sol3 = board.get_pin("d:50:o")  # Solenoid 3 Pins
blow = board.get_pin("d:51:o")  # Head Blow Solenoid 4
stop = board.get_pin("d:52:o")  # Stopper (Stops air loss) Solenoid 5

# pinShort = board.get_pin("d:57:i")
# pinLong = board.get_pin("d:56:i")
# plastic = board.get_pin("d:58:i")
# heightSensor = board.get_pin("d:55:i")

# Putting Outputs to zero
print("Zero")
enable.write(1)
blow.write(0)
stop.write(0)
sol2.write(0)
sol3.write(0)

time.sleep(2)
while True:
    print("High")
    suction.write(1)
    blow.write(1)
    stop.write(1)
    sol2.write(1)
    sol3.write(1)
    for i in range(5):
        print(i)
        time.sleep(1)

    print("Zero")
    suction.write(0)
    blow.write(0)
    stop.write(0)
    sol2.write(0)
    sol3.write(0)
    for i in range(5):
        print(i)
        time.sleep(1)
