import subprocess
import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
com = 'COM2'
for p in ports:
    if 'USB Serial Device' in p.description:
        com = str(p[0])
        # print(com)

        result = subprocess.run(r'C:\Users\michael.guerrero\PycharmProjects\CodingProblems\BLEDongleFW_VER 1.9.0.0_20191125\dev\FwUpdateApp.exe {} DONGLEFW'.format(com), stdout=subprocess.PIPE)
        serialNumber = str(result).split("Serial Number = ", 1)[1][:6]
        print(serialNumber)

