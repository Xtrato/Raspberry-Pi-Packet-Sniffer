import time
import subprocess
from subprocess import call
from datetime import datetime
fileName = str(datetime.now().day) + "-" + str(datetime.now().month) + "-" + str(datetime.now().year) + " AT " + str(datetime.now().hour) + "-" + str(datetime.now().minute)
while True:
    tcpDumpProcess = subprocess.call(["tcpdump", "-w", fileName, "-i", "eth0"])
    currentHour = datetime.now().minute
    while True:
        if datetime.now().minute != currentHour:
            tcpDumpProcess.terminate()
            print "CHJAMNGE"
            break
