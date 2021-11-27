import socket

print("""  ___                _    ___                            
 / __|_ __  ___  ___| |__/ __| __ __ _ _ _  _ _  ___ _ _ 
 \__ \ '_ \/ _ \/ _ \ / /\__ \/ _/ _` | ' \| ' \/ -_) '_|
 |___/ .__/\___/\___/_\_\|___/\__\__,_|_||_|_||_\___|_|  
     |_|                                                 
     """)

print("""                            
             Created By SEMPATİK       
         ╚────────────────────────────╝
      """)

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




