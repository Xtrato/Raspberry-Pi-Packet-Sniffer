import subprocess
from dbupload import upload_file #Used for Dropbox uploading
from datetime import datetime # Used the genreate the filename
count = 0 #Counts the number of files that have been dumped
while True:
    count = count + 1
    fileName = str(datetime.now().day) + "-" + str(datetime.now().month) + "-" + str(datetime.now().year) + " AT " + str(datetime.now().hour) + "-" + str(datetime.now().minute)
    tcpDumpProcess = subprocess.Popen(["tcpdump", "-Z", "root", "-w", fileName, "-i", "bridge0", "-G", "60", "-W", "1"]) #Sets up the TCPDump command
    tcpDumpProcess.communicate() #Runs the TCPDump command
    print "Currently dumping file number " + str(count) + "."
    upload_file(fileName,"/",fileName, "YOUR_EMAIL","YOUR_PASSWORD") #Uploads the dump file to dropbox
    print "File uploaded Successfully"
