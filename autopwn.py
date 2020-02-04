#!/usr/bin/python3

import os
import sys
import time
import re
import nmap
import requests
import subprocess
from progressbar import ProgressBar, Bar, Percentage
from colorama import Fore, Back, Style


if os.geteuid() != 0:
    print("\n" + Fore.RED + "[!] Use sudo to run your script !\n")
    time.sleep(1)
    exit(1)

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
                print("\n[+] Let's pwn !\n")
                mainPwn(ip)

        elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
            os.system('clear')
            help()

        elif re.match(regex,sys.argv[1]):
            ip = sys.argv[1]
            os.system('clear')
            print("\n[!] Let's pwn !\n")
            mainPwn(ip)

        else:
            print("\n[!] Wrong input..")
            time.sleep(1)
            os.system('clear')
            help()

def mainPwn(ip):
    print("[+] Doing Nmap scan ...")
    nmapScan(ip)


def nmapScan(ip):
    dirb = False
    rangePort = '1-1000'
    nmScan = nmap.PortScanner()
    try:
        nmScan.scan(ip,rangePort)
    except:
        exit(Fore.RED+"[!] An error has occured, try again later ...")

    for host in nmScan.all_hosts():
        print('\n    Host : %s ' % host)
        print(Fore.GREEN+'    State : %s' % (nmScan[host].state())+Style.RESET_ALL)

        for proto in nmScan[host].all_protocols():
            print("\n    ---------------------\n")
            print('    Protocol : %s' % proto)

            lport = nmScan[host][proto].keys()
            for port in lport:
                if port == 80:
                    dirb = True
                state = nmScan[host][proto][port]['state']
                if state != 'closed':
                    print(Fore.GREEN+'    [!] port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))

    print(Style.RESET_ALL)
    if dirb == True:
        dirbScan(ip)

def dirbScan(ip):
    print("[+] Starting dirb ...\n")
    list_allowed_code = ["200","201","204","300","301","302","303","304"]
    loading = "#"
    list_founded_dirs = []
    num_founded_dirs = 0
    extension = ["/",".php", ".html"]
    index = 0

    nber_lines = str(subprocess.run(["wc", "-l", "directory-list-2.3-medium.txt"], stdout=subprocess.PIPE))
    nber_lines1 = nber_lines.split("stdout=b'")[1]
    nber_lines2 = nber_lines1.split(" ")[0]

    nber_lines = int(nber_lines2)

    pBar = ProgressBar(widgets=[Percentage(), Bar()], maxval=nber_lines).start()

    try :
        with open("directory-list-2.3-medium.txt", "r") as check_list:
            for line in pBar(check_list):
                index += 1

                for ext in extension :
                    site_to_test = "http://" + ip + '/' + line.replace("\n","") + ext
                    site_request = requests.get(site_to_test)

                    if (str(site_request.status_code) in list_allowed_code) == True :
                        list_founded_dirs.append(site_to_test)
                        num_founded_dirs += 1

    except KeyboardInterrupt:
        pBar.finish()
        print("\n")
        print("Directory / files found : \n")
        for dirs in list_founded_dirs:
            print(Fore.GREEN+'    [!] '+dirs)

        exit(1)

    print("\n")
    print("    Directory / files found \n")
    for dirs in list_founded_dirs:
        print(Fore.GREEN+'    [!] '+dirs)

    print(Style.RESET_ALL)

command()
