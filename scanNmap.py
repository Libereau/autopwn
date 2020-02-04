import nmap
from colorama import Fore, Back, Style
from dirbScan import dirbscan


def nmapScan(ip):
    print("[+] Doing Nmap scan ...")
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
                    print(Fore.GREEN+'    [!] port : %s - state : %s' % (port, nmScan[host][proto][port]['state']))
                    print('        %s - %s' % (nmScan[host][proto][port]['name'], nmScan[host][proto][port]['version']))

    print(Style.RESET_ALL)
    if dirb == True:
        dirbscan(ip)
