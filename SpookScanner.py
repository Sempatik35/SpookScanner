import socket

import random,time, sys
from colorama import *
 
init(autoreset=True)
fr = Fore.RED
fb = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
 
def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
 
    x = """
  ___                _    ___                            
 / __|_ __  ___  ___| |__/ __| __ __ _ _ _  _ _  ___ _ _ 
 \__ \ '_ \/ _ \/ _ \ / /\__ \/ _/ _` | ' \| ' \/ -_) '_|
 |___/ .__/\___/\___/_\_\|___/\__\__,_|_||_|_||_\___|_|  
     |_|                    
 
       +--------CREATED BY SEMPATİK--------+
 
                                          """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
        time.sleep(0.06)
logo()

site = input("Site url: ")
target = socket.gethostbyname(site)

print("-" * 45)
print("scanned site ip: " + target)
print("-" * 45)

try:
    for port in range(1, 65500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port,))
        if result == 0:
           print("Port {} open".format(port))
        s.close()
except Exception as e:
    print(Error , e)





