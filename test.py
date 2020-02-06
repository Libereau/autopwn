import subprocess
import os, re


def dirList() :

    regexUrl = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    try :
        with open("sortie.txt") as f:
            lines = f.readlines()
            #print(lines)

        #data = re.findall('name="(.*?)"',parameters)
            for line in lines:
                #print(line)
                url = re.findall(regexUrl,line)

                if url != []:
                    print(url[0])

    except:
        exit(1)


dirList()
