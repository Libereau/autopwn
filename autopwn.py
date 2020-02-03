#!/usr/bin/python3

import os
import sys
import time
import re
from colorama import Fore, Back, Style

if os.geteuid() != 0:
    print("\n" + Fore.RED + "[!] Use sudo to run your script !\n")
    time.sleep(1)
    exit(1)

os.system('clear')

def command():
    regex = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

    if len(sys.argv) < 2:
        print("[+] Don't forget to use -h or --help if needed !")
        help()

    else :
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            help()
        elif re.match(regex,sys.argv[1]):
            print("\n[x] Let's pwn !\n")
        else:
            print("\n[!] Wrong input..")
            time.sleep(1)
            os.system('clear')
            help()

def help():
    print("-----------------------------------------------------------\n")
    print("                        Autopwn                       \n")
    print("-----------------------------------------------------------\n")
    print("[!] How to use autopwn : ")
    print("    Next to ./autopwn precise the ip address you try to pwn")
    print("    Example : ./autopwn 192.168.1.1\n")
    print("    Then go have a coffee :D \n")
    print("-----------------------------------------------------------\n")

command()
