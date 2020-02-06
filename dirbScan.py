import subprocess
import requests
from progressbar import ProgressBar, Bar, Percentage
from colorama import Fore, Back, Style
from parsingFilesDirs import parsingFiles

def dirbscan(ip):
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
        print("\n    Directory / files found : \n")
        for dirs in list_founded_dirs:
            print(Fore.GREEN+'    [!] '+dirs)

        print("\n"+Style.RESET_ALL)
        parsingFiles(list_founded_dirs)

    print("\n    Directory / files found \n")
    for dirs in list_founded_dirs:
        print(Fore.GREEN+'    [!] '+dirs)

    print(Style.RESET_ALL)

    parsingFiles(list_founded_dirs)
