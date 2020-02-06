#!/usr/bin/python3

import time
import os
from commandMain import command
from colorama import Fore, Back, Style

# Utilisation de Konan

if os.geteuid() != 0:
    print("\n" + Fore.RED + "[!] Use sudo to run your script !\n")
    time.sleep(1)
    exit(1)


def main():
    command()

if __name__ == '__main__':
    main()
