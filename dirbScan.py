import os, re
from colorama import Fore, Back, Style
from parsingFilesDirs import parsingFiles

def dirbscan(ip):
    print("[+] Starting dirb ...\n")
    list_founded_dirs = []

    cmd = "python3 /home/libero/Konan/konan.py -u http://"+ip+" -x 403 > /home/libero/Documents/programmes/autopwn/sortie.txt"
    os.system(cmd)
    regexUrl = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    #try :
    with open("sortie.txt") as f:
        lines = f.readlines()

        for line in lines:
            url = re.findall(regexUrl,line)

            if url != []:
                list_founded_dirs.append(url[0])

    for a in list_founded_dirs:
        print(Fore.GREEN+"     [!] %s" % a)

    print(Style.RESET_ALL+"\n")
    parsingFiles(list_founded_dirs)

    #except Exception:
    #    exit("An error has occured...")
