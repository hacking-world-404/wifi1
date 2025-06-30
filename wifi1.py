from os import system as c
import time
import random

# Colors
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
P = '\x1b[38;5;201m'

def logo():
    c('clear')
    print(f"""{C}
 ▄▄▄▄▄  ▄▄▄▄▄  ▄▄▄▄▄ 
▐█   █▌▐█   █▌▐█    
▐█▀▀▀  ▐█▀▀▀  ▐█▀▀▀ 
▐█     ▐█     ▐█▄▄▄ 

{P} HACKING WORLD - WIFI PASSWORD VIP TOOL (ROOT)
""")

def loading(task, sec):
    print(f"{Y}[+] {task}")
    for i in range(sec):
        print(f"{G}[*] Working{'.' * (i % 4)}")
        time.sleep(1)

def wifi_hack():
    logo()
    cookie = input(f"{C}ENTER YOUR VIP COOKIE: ")
    loading("Verifying Cookie", 2)
    print(f"{G}[✓] Cookie Verified!\n")
    ssid = input(f"{C}ENTER TARGET WIFI NAME (SSID): ")
    loading(f"Connecting to {ssid}", 3)
    print(f"{G}[✓] Connected to {ssid}!\n")
    loading("Cracking Password", 5)
    fake_pass = random.choice(["pass2025", "wifi@hack", "adminwifi123", "vipaccess999"])
    print(f"{P}[✓] PASSWORD FOUND: {Y}{fake_pass}\n")
    input(f"{A}Press Enter To Return To Menu...")
    menu()

def menu():
    logo()
    print(f"{A}[1] Start WiFi Password (ROOT)")
    print(f"{A}[0] Exit Tool")
    choice = input(f"{Y}Select Option: ")
    if choice == '1':
        wifi_hack()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] Invalid Option!")
        time.sleep(1)
        menu()

menu()