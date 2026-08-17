import os

RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = "\033[93m"
WHITE = "\033[97m"
RESET = '\033[0m'


print(f"""{RED}
  █████████     ██████   █████    ███████████     ███████████     
 ███▒▒▒▒▒███   ▒▒██████ ▒▒███    ▒▒███▒▒▒▒▒███   ▒▒███▒▒▒▒▒███    
▒███    ▒▒▒     ▒███▒███ ▒███     ▒███    ▒███    ▒███    ▒███    
▒▒█████████     ▒███▒▒███▒███     ▒██████████     ▒██████████     
 ▒▒▒▒▒▒▒▒███    ▒███ ▒▒██████     ▒███▒▒▒▒▒▒      ▒███▒▒▒▒▒███    
 ███    ▒███    ▒███  ▒▒█████     ▒███            ▒███    ▒███    
▒▒█████████     █████  ▒▒█████    █████           █████   █████   
 ▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒           ▒▒▒▒▒   ▒▒▒▒▒                                                                                                                                       
{RESET}  

  {GREEN}Coded by SNPR 
  github: https://github.com/YAHYA-DEV75{RESET}

{YELLOW}
   Version: 1        CTRL+C: exit        Author: SNPR{RESET}

 {BLUE}[1]{RESET} {WHITE}Zphisher{RESET}            {BLUE}[2]{RESET} {WHITE}Nmap{RESET}
 {BLUE}[3]{RESET} {WHITE}Wireshark{RESET}           {BLUE}[4]{RESET} {WHITE}Metasploit{RESET}    
 {BLUE}[5]{RESET} {WHITE}Hydra{RESET}               {BLUE}[6]{RESET} {WHITE}Sqlmap{RESET}
 {BLUE}[7]{RESET} {WHITE}John the ripper{RESET}     {BLUE}[8]{RESET} {WHITE}Burp suite{RESET}
 {BLUE}[9]{RESET} {WHITE}Wifite2{RESET}             {BLUE}[10]{RESET} {WHITE}Netcat{RESET}
 {BLUE}[11]{RESET} {WHITE}Aircrack-ng{RESET}        {BLUE}[12]{RESET} {WHITE}Bettercap{RESET}
 {BLUE}[13]{RESET} {WHITE}Setoolkit{RESET}          {BLUE}[14]{RESET} {WHITE}Hashcat{RESET}
 
 
""")

choice = input("choice your tool to install:")

if choice =="1":
    os.system("git clone https://github.com/htr-tech/zphisher.git")

if choice =="2":
    os.system("git clone https://github.com/nmap/nmap.git")

if choice =="3":
    os.system("git clone https://github.com/wireshark/wireshark.git")

if choice =="4":
    os.system("git clone https://github.com/rapid7/metasploit-framework.git")

if choice =="5":
    os.system("git clone https://github.com/vanhauser-thc/thc-hydra.git")

if choice =="6":
    os.system("git clone https://github.com/sqlmapproject/sqlmap.git")

if choice =="7":
    os.system("git clone https://github.com/openwall/john.git")

if choice =="8":
    os.system("git clone https://github.com/xiv3r/Burpsuite-Professional.git")

if choice =="9":
    os.system("git clone https://github.com/derv82/wifite2.git")

if choice =="10":
    os.system("git clone https://github.com/H74N/netcat-binaries.git")

if choice =="11":
    os.system("git clone https://github.com/aircrack-ng/aircrack-ng.git")

if choice =="12":
    os.system("git clone https://github.com/bettercap/bettercap.git")

if choice =="13":
    os.system("git clone https://github.com/trustedsec/social-engineer-toolkit.git")

if choice =="14":
    os.system("git clone https://github.com/hashcat/hashcat.git")