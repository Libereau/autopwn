import requests
import re
from colorama import Fore, Back, Style


def parsingFiles(list_founded_dirs):

    print("[+] Parsing files and dirs..")

    listFiles = list_founded_dirs

    #for file in listFiles:
        #print(Fore.GREEN+"    [!] %s" % file+Style.RESET_ALL)

    for file in listFiles:

        response = requests.get(file)
        response.encoding = 'utf-8'
        cont = response.text


        if "form" in cont:
            a = cont.split("<form ")[1]

            print(Fore.RED+"\n    [!] Forms on '%s' : " % file+Style.RESET_ALL)

            data = re.findall('name="(.*?)"',a)
            print("        Parameters used : %s" % data)


    print("\n")

list_founded_dirs = ["http://127.0.0.1/index.html","http://127.0.0.1/glossary/","http://127.0.0.1/connexion.php","http://127.0.0.1/command.php"] #
parsingFiles(list_founded_dirs)
