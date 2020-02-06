import subprocess
import os, re


def dirList() :
    print("\nDirb scan ..\n")
    list_founded_dirs = []
    #
    #cmd = "python3 /home/libero/Konan/konan.py -u http://127.0.0.1 -x 403 > /home/libero/Documents/programmes/autopwn/sortie.txt"
    #os.system(cmd)
    regexUrl = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    try :
        with open("sortie.txt") as f:
            lines = f.readlines()

            for line in lines:
                url = re.findall(regexUrl,line)

                if url != []:
                    list_founded_dirs.append(url[0])

        for a in list_founded_dirs:
            print("     [!] %s" % a)

        print("\n")
    except Exception:
        exit(1)


dirList()
