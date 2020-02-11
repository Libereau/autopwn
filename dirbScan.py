import os, re, subprocess
from colorama import Fore, Back, Style
from parsingFilesDirs import parsingFiles

def dirbscan(ip):
    print("[+] Starting dirb ... (may take some times)\n")
    list_founded_dirs = []
    chemin = str(subprocess.run(['pwd',"/dev/null"], capture_output=True)).split("stdout=b'")[1].split("\\n', stderr=b'")[0]

    cmd = "python3 /root/Konan/konan.py -u http://"+ip+" -x 403 > "+chemin+"/sortie.txt"
    os.system(cmd)

    regexUrl = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    with open("sortie.txt") as f:
        lines = f.readlines()

        for line in lines:
            url = re.findall(regexUrl,line)

            if url != [] :
                if len(url) != 1 :
                    list_founded_dirs.append(url[1])
                else:
                    list_founded_dirs.append(url[0])

    list_founded_dirs = set(list_founded_dirs)

    for a in list_founded_dirs:
        print(Fore.GREEN+"     [!] %s" % a)

    print(Style.RESET_ALL+"\n")
    parsingFiles(list_founded_dirs)

#dirbscan('127.0.0.1')
