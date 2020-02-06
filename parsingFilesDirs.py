import requests
import re
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style


def parsingFiles(list_founded_dirs):
    blacklist = ["form_id","form_build_id","search_block_form","audience","technical"]

    print("[+] Parsing files and dirs..")

    listFiles = list_founded_dirs

    for file in listFiles:
        response = requests.get(file)
        soup = BeautifulSoup(response.text,"lxml")

        if soup.form != None:

            a = soup.findAll("input")

            parameters = str(soup.findAll("input"))
            print(Fore.RED+"\n    [!] Forms on '%s' : " % file+Style.RESET_ALL)
            data = re.findall('name="(.*?)"',parameters)

            data = set(data)
            for element in blacklist :
                if element in data:
                    data.remove(element)

            print("        Parameters used : %s" % data)

def parsingUrl(list_founded_dirs):



#list_founded_dirs = ["http://192.168.7.12/contact/","http://127.0.0.1/command.php"]
#"http://127.0.0.1/glossary/","http://127.0.0.1/connexion.php","http://127.0.0.1/command.php"] #
#parsingFiles(list_founded_dirs)
