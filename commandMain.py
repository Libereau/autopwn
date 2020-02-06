import re
import os
import sys
import time
from scanNmap import nmapScan
from colorama import Fore, Back, Style


def help():
    print("-----------------------------------------------------------\n")
    print("                        Autopwn                       \n")
    print("-----------------------------------------------------------\n")
    print("[!] How to use autopwn : ")
    print("    Next to ./autopwn precise the ip address you try to pwn")
    print("    Example : ./autopwn 192.168.1.1\n")
    print("    Then go have a coffee :D \n")
    print("-----------------------------------------------------------\n")


def command():
    regex = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

    if len(sys.argv) < 2:
        print("[+] Don't forget to use -h or --help if needed !")
        help()

    else :
        if sys.argv[0] == 'sudo' :
            if sys.argv[2] == "-h" or sys.argv[2] == "--help":
                os.System('clear')
                help()

            elif re.match(regex,sys.argv[2]):
                ip = sys.argv[2]
                os.system('clear')
                print("\n---------------- AutoPwn ----------------")
                print("\n[!] Let's pwn !\n")
                nmapScan(ip)

        elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
            os.system('clear')
            help()

        elif re.match(regex,sys.argv[1]):
            ip = sys.argv[1]
            os.system('clear')
            print("\n---------------- AutoPwn ----------------")
            print("\n[!] Let's pwn !\n")
            nmapScan(ip)

        else:
            print("\n[!] Wrong input..")
            time.sleep(1)
            os.system('clear')
            help()

    print(Style.RESET_ALL)
