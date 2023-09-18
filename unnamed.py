class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[31m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
import shutil
import os
import time
import subprocess
import urllib.request
import re
import hashlib
import zipfile
import random
import string

try:
    
    import requests
    try:
        import pyfiglet
    except:
        import os
        os.system("clear")
        os.system("cls")
        print(bcolors.FAIL + f"[{bcolors.ENDC}MODULES{bcolors.FAIL}] Missing modules")
        print()
        input(f"Try: '{bcolors.ENDC}pip install pyfiglet{bcolors.FAIL}' \n")
        os.system("clear")
        os.system("cls")
        exit()
except:
    import os
    try:
        import pyfiglet
        columns = shutil.get_terminal_size().columns
        error = pyfiglet.figlet_format("ERROR", font='3d-ascii')
        os.system("clear")
        os.system("cls")
        print(bcolors.FAIL + error)
        print(bcolors.FAIL + f"[{bcolors.ENDC}MODULES{bcolors.FAIL}] Missing modules".center(columns))
        print()
        input(f"Try: '{bcolors.ENDC}pip install requests{bcolors.FAIL}' \n")
        exit()
    except:
        import os
        os.system("clear")
        os.system("cls")
        print(bcolors.FAIL + f"[{bcolors.ENDC}MODULES{bcolors.FAIL}] Missing modules")
        print()
        input(f"Try: '{bcolors.ENDC}pip install pyfiglet{bcolors.FAIL}' and '{bcolors.ENDC}pip install requests{bcolors.FAIL}' or install now \n")
        os.system("clear")
        os.system("cls")
        exit()
    

columns = shutil.get_terminal_size().columns

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
atem = 0
guess = ''
url = 'https://raw.githubusercontent.com/HSp4m/UnnamedM/main/version.txt'
#urlD = "https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/HSp4m/UnnamedM/blob/main/unnamed.py"
query_parameters = {"downloadformat": "py"}
page = urllib.request.urlopen(url)
c_version = "0.0.8"
u_version = f"{page.read()}".replace("b","").replace("'","").replace("n","").replace("\\","")
p_enabled = False;

def crack(zip_file, path, val):

    os.system("clear")
    os.system("cls")

    print(bcolors.FAIL + pyfiglet.figlet_format("Craking...", font='3d-ascii', width=110, justify="center"))
    print("------------------------------------------------------------------------------------".center(columns))

    atem = 0
    while True:
        if val == "0":
            input("a")
            guess = ''.join(random.choices(string.ascii_letters + string.digits, k=int(string.digits))).encode('utf-8')
        else:
            guess = ''.join(random.choices(string.ascii_letters + string.digits, k=int(val))).encode('utf-8')
            
        atem += 1
        try:

            zip_file.extractall(path,pwd=guess)

            os.system("clear")
            os.system("cls")

            print(bcolors.OKGREEN + pyfiglet.figlet_format("Craked !", font='3d-ascii', width=110, justify="center"))
            print("------------------------------------------------------------------------------------".center(columns))
            print()
            print(f"Password: {guess} attempts: {atem}".center(columns))
            print()
            break

        except:
            continue

def crackP(zip_file, path, pathP):

    os.system("clear")
    os.system("cls")
    total = len(list(open(pathP)))
    atem = 0
    crack = 0
    print(bcolors.FAIL + pyfiglet.figlet_format("Craking...", font='3d-ascii', width=110, justify="center"))
    print("------------------------------------------------------------------------------------".center(columns))
    print()
    print(f"[{bcolors.ENDC}INFO{bcolors.FAIL}] Trying '{total}' passwords.".center(columns))

    with open(pathP, "rb") as file:
        for line in file:
            for guees in line.split():
                try:
                    atem +=1
                    zip_file.extractall(path,pwd=guees)
                    crack = 1
                    os.system("clear")
                    os.system("cls")
                    print(bcolors.OKGREEN + pyfiglet.figlet_format("Craked !", font='3d-ascii', width=110, justify="center"))
                    print("------------------------------------------------------------------------------------".center(columns))
                    print()
                    print(f"Password: {guees.decode()} Line: {atem}".center(columns))
                    print()
                    break

                except:
                    continue
    if atem == total:
        if crack == 0:
            os.system("clear")
            os.system("cls")
            print(bcolors.FAIL + pyfiglet.figlet_format("Not Found !", font='3d-ascii', width=110, justify="center"))
            print("------------------------------------------------------------------------------------".center(columns))
            print()
            print(f"Password not found in Password List.".center(columns))
            input("\n: ")
            loader(menu)




def malwares():
    os.system("clear")
    os.system("cls")
    print(bcolors.FAIL + pyfiglet.figlet_format("Malware", font='3d-ascii', width=110, justify="center"))
    print("------------------------------------------------------------------------------------".center(columns))
    print()
    print(f"[{bcolors.ENDC}01{bcolors.FAIL}]. List Malwares".center(columns))
    print(f"[{bcolors.ENDC}00{bcolors.FAIL}]. Quit".center(columns))
    print()
    value = input(bcolors.ENDC +"Select: ")

    if value in ["0", "00"]:
        loader(menu)
    if value in ["1", "01"]:
        loader(menu)

def firewall():
    os.system("clear")
    os.system("cls")
    print(bcolors.FAIL + pyfiglet.figlet_format("Firewall", font='3d-ascii', width=110,justify="center"))
    print("------------------------------------------------------------------------------------".center(columns))
    print()
    print(f"[{bcolors.ENDC}01{bcolors.FAIL}] Enable ".center(columns))
    print(f"[{bcolors.ENDC}02{bcolors.FAIL}] Disable ".center(columns))
    print(f"[{bcolors.ENDC}00{bcolors.FAIL}] Quit ".center(columns))
    print()

    value = input(bcolors.ENDC + "Select: ")

    if value in ["0", "00"]:
        loader(menu)

    elif value in ["1", "01"]:
        os.system("clear")
        os.system("cls")

        os.system("netsh advfirewall set allprofiles state on")

        os.system("clear")
        os.system("cls")

        print(f"[{bcolors.OKGREEN}ON{bcolors.ENDC}] Firewall".center(columns))

        time.sleep(5)
        loader(menu)

    elif value in ["2", "02"]:
        os.system("clear")
        os.system("cls")

        os.system("netsh advfirewall set allprofiles state off")

        os.system("clear")
        os.system("cls")

        print(f"[{bcolors.FAIL}OFF{bcolors.ENDC}] Firewall".center(columns))
        
        time.sleep(5)
        loader(menu)
    
def about():
    os.system("clear")
    os.system("cls")
    print(bcolors.FAIL + pyfiglet.figlet_format("HSP4M", font='3d-ascii', justify="center"))
    print("------------------------------------------------------------------------------------".center(columns))
    print()  
    print("https://github.com/HSp4m".center(columns))
    print()
    print(f"Version: [{bcolors.ENDC}BETA {c_version}{bcolors.FAIL}]".center(columns))
    
    input("\n:")
    loader(menu)


def commands():
    os.system("clear")
    os.system("cls")
    print(bcolors.FAIL + pyfiglet.figlet_format("Commands", font='3d-ascii', width=110, justify="center"))
    print("------------------------------------------------------------------------------------".center(columns))
    print()
    print(f"[{bcolors.ENDC}01{bcolors.FAIL}]. Taskkill".center(columns))
    print(f"[{bcolors.ENDC}00{bcolors.FAIL}]. Quit".center(columns))
    print()

    value = input("Select: ")

    if value in ["0", "00"]:
        loader(menu)

    if value in ["1", "01"]:
        loader(menu)

def vrchat():
    os.system("clear")
    os.system("cls")
    print(bcolors.FAIL + pyfiglet.figlet_format("VRChat", font='3d-ascii', width=110, justify="center"))


    value = input("VRChat Folder: " + bcolors.ENDC)
    if os.path.isdir(value):
        os.system("clear")
        os.system("cls")
        print(bcolors.ENDC +f"[{bcolors.OKBLUE}INFO{bcolors.ENDC}] Starting Path Verification.".center(columns))
        print()
        if os.path.isfile(f"{value}\VRChat.exe"):
            print(f"[{bcolors.OKGREEN}OK{bcolors.ENDC}] Game executable".center(columns))
            print()

            if os.path.isfile(f"{value}\start_protected_game.exe"):
                print(f"[{bcolors.OKGREEN}OK{bcolors.ENDC}] AntiCheat executable".center(columns))
                input()
            else:
                print(f"[{bcolors.FAIL}ERROR{bcolors.ENDC}] AntiCheat executable".center(columns))
                print("Press ANY key to continue.")
                input()
                print()
                menu()

        else:
            print(f"[{bcolors.FAIL}ERROR{bcolors.ENDC}] Game executable".center(columns))
            print("Press ANY key to continue.")
            input()
            print()
            menu()
    else:
        os.system("clear")
        os.system("cls")
        print(f"{bcolors.FAIL}[{bcolors.ENDC}{value}{bcolors.FAIL}] it's not a valid folder.".center(columns))
        print()
        input("Press ANY key to continue.")
        print()
        loader(menu)

def password():
    os.system("clear")
    os.system("cls")
    print(bcolors.FAIL + pyfiglet.figlet_format("Passwords. Cracker", font='3d-ascii', width=110, justify="center"))
    print("------------------------------------------------------------------------------------".center(columns))
    print()
    print(f"[{bcolors.ENDC}01{bcolors.FAIL}]. WIFI bruteforce    ".center(columns))
    print(f"[{bcolors.ENDC}02{bcolors.FAIL}]. Hash Decrypter     ".center(columns))
    print(f"[{bcolors.ENDC}03{bcolors.FAIL}]. Zip Decrypter     ".center(columns))
    print(f"[{bcolors.ENDC}00{bcolors.FAIL}]. Quit               ".center(columns))
    print()

    value = input(bcolors.ENDC + "Select: ")

    if value in ["0", "00"]:
        loader(menu)

    elif value in ["1", "01"]:
        loader(menu)

    elif value in ["2", "02"]:
        os.system("clear")
        os.system("cls")
        print(bcolors.FAIL + pyfiglet.figlet_format("Password. Hash", font='3d-ascii', width=110, justify="center"))
        print("------------------------------------------------------------------------------------".center(columns))
        print()
        print(f"[{bcolors.ENDC}01{bcolors.FAIL}]. MD5         ".center(columns))
        print(f"[{bcolors.ENDC}02{bcolors.FAIL}]. SHA-256     ".center(columns))
        print(f"[{bcolors.ENDC}03{bcolors.FAIL}]. SHA-1       ".center(columns))
        print(f"[{bcolors.ENDC}00{bcolors.FAIL}]. Quit        ".center(columns))
        print()

        value = input(bcolors.ENDC + "Select: ")

        if value in ["0", "00"]:
            loader(menu)

        elif value in ["1", "01"]:
            os.system("clear")
            os.system("cls")
            print(bcolors.FAIL + pyfiglet.figlet_format("Password. Hash", font='3d-ascii', width=110, justify="center"))
            print("------------------------------------------------------------------------------------".center(columns))
            print()
            value = input("Hash (MD5): ")

            if value != "":
                d = hashlib.md5.new(value)
                d.update(value)
                print(d.hexdigest())
                input()
                loader(menu)

        elif value in ["2", "02"]:
            loader(menu)

        elif value in ["3", "03"]:
            loader(menu)

    elif value in ["3", "03"]:
        os.system("clear")
        os.system("cls")
        print(bcolors.FAIL + pyfiglet.figlet_format("Zip. Cracker", font='3d-ascii', width=110, justify="center"))
        print("------------------------------------------------------------------------------------".center(columns))
        print()
        print(f"[{bcolors.ENDC}01{bcolors.FAIL}]. Random numbers    ".center(columns))
        print(f"[{bcolors.ENDC}02{bcolors.FAIL}]. Password list     ".center(columns))
        print(f"[{bcolors.ENDC}00{bcolors.FAIL}]. Quit              ".center(columns))
        print()

        value = input("Select: ")

        if value in ["1", "01"]:
            os.system("clear")
            os.system("cls")

            print(bcolors.FAIL + pyfiglet.figlet_format("Zip. Cracker", font='3d-ascii', width=110, justify="center"))
            print("------------------------------------------------------------------------------------".center(columns))
            print()

            value = input("Zip Path: ")

            if os.path.isfile(value):
                value2 = input("\nPath to extract: ")

                if os.path.isdir(value2):
                    val = input("\nCharacters amount: ")
                    zip_value = zipfile.ZipFile(value, mode="r")
                    crack(zip_value,value2,val)

                else:
                    print(f"{bcolors.FAIL}[{bcolors.ENDC}ERROR{bcolors.FAIL}] Invalid Folder Path".center(columns))
                    input("\n:")
                    loader(password)

            else:
                print(f"{bcolors.FAIL}[{bcolors.ENDC}ERROR{bcolors.FAIL}] Invalid Zip Path".center(columns))
                input("\n:")
                loader(password)

        elif value in ["2", "02"]:

            os.system("clear")
            os.system("cls")

            print(bcolors.FAIL + pyfiglet.figlet_format("Zip. Cracker", font='3d-ascii', width=110, justify="center"))
            print("------------------------------------------------------------------------------------".center(columns))
            print()
            value = input("Password list path: ")

            if os.path.isfile(value):
                value2 = input("\nZip Path: ")

                if os.path.isfile(value2):
                    value3 = input("\nPath to extract: ")

                    if os.path.isdir(value3):
                        zip_file = zipfile.ZipFile(value2, mode="r")
                        crackP(zip_file,value3,value)

                    else:

                        print(f"{bcolors.FAIL}[{bcolors.ENDC}ERROR{bcolors.FAIL}] Invalid Folder Path".center(columns))
                        input("\n:")
                        loader(password)
                else:

                    print(f"{bcolors.FAIL}[{bcolors.ENDC}ERROR{bcolors.FAIL}] Invalid Zip Path".center(columns))
                    input("\n:")
                    loader(password)
            else:

                print(f"{bcolors.FAIL}[{bcolors.ENDC}ERROR{bcolors.FAIL}] Invalid Password list Path".center(columns))
                input("\n:")
                loader(password)

        elif value in ["0", "00"]:

            loader(menu)

        else:

            loader(password)

    
def menu():

    os.system("clear")
    os.system("cls")
    print(bcolors.FAIL + pyfiglet.figlet_format("Crow 61", font='3d-ascii', justify="center"))
    print(bcolors.FAIL +f" [{bcolors.ENDC}01{bcolors.FAIL}].  Malwares                       ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +f" [{bcolors.ENDC}02{bcolors.FAIL}].  Windows Firewall               ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +f" [{bcolors.ENDC}03{bcolors.FAIL}].  Passwords                      ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +f" [{bcolors.ENDC}04{bcolors.FAIL}].  VRChat [EAC Bypassed]          ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +f" [{bcolors.ENDC}05{bcolors.FAIL}].  Commands                       ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +f" [{bcolors.ENDC}99{bcolors.FAIL}].  About                          ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +f" [{bcolors.ENDC}00{bcolors.FAIL}].  Quit                           ".center(columns) +bcolors.ENDC)
    print()
    print()

    value = input("Select: ")


    if value in  ["1", "01"] :
        os.system("clear")
        os.system("cls")
        malwares()

    elif value in  ["2", "02"]:
        firewall()

    elif value in  ["3", "03"]:
        os.system("clear")
        os.system("cls")
        password()

    elif value in  ["4", "04"]:
        os.system("clear")
        os.system("cls")
        vrchat()

    elif value in  ["5", "05"]:
        os.system("clear")
        os.system("cls")
        commands()

    elif value == "99":
        os.system("clear")
        os.system("cls")
        
        about()

    elif value in  ["0", "00"]:
        exit()
    else:
        os.system("clear")
        os.system("cls")
        print(f"[{bcolors.ENDC}{value}{bcolors.FAIL}] it's not a valid input.".center(columns))
        print()
        input("Press ANY key to continue.")
        print()
        menu()

page = urllib.request.urlopen(url)
u_version = f"{page.read()}".replace("b","").replace("'","").replace("n","").replace("\\","")

def loader(fnc):
    os.system("clear")
    os.system("cls")
    page = urllib.request.urlopen(url)
    u_version = f"{page.read()}".replace("b","").replace("'","").replace("n","").replace("\\","")
    if (u_version == c_version):
        fnc()

    elif (u_version < c_version):
        
        print(bcolors.FAIL + pyfiglet.figlet_format("Updater", font='3d-ascii', justify="center").center(columns))
        print("Invalid version detected.".center(columns))
        print()
        print(f"Current version: [{bcolors.ENDC}{c_version}{bcolors.FAIL}]".center(columns))
        print(f"Latest version: [{bcolors.ENDC}{u_version}{bcolors.FAIL}]".center(columns))
        print()

        value = input(f"{bcolors.ENDC}Fix? [{bcolors.OKGREEN}Y{bcolors.ENDC}/{bcolors.FAIL}N{bcolors.ENDC}]: ")

        if value in ["N", "n"]:
            fnc()
        elif value in ["S", "s", "Y", "y"]:
            if os.path.isdir("UnnamedM\\"):
                if os.path.isfile("UnnamedM\\unnamed.py"):
                    os.system("cls")
                    os.system("clear")
                    print(bcolors.ENDC + f"[{bcolors.OKBLUE}INFO{bcolors.ENDC}] A possible updated file exist in 'UnnamedM\\unnamed.py'.".center(columns))
                    print(bcolors.ENDC + f"[{bcolors.OKBLUE}INFO{bcolors.ENDC}] Delete folder if you want update again.".center(columns))
                    input("\nPress any key to continue \n")
                    exit()
            
            os.system("clear")
            os.system("cls")
            print(bcolors.FAIL + pyfiglet.figlet_format("UP. Options", font='3d-ascii', justify="center").center(columns))
        
            print(bcolors.FAIL +f" [{bcolors.ENDC}1{bcolors.FAIL}].  Download (Not working)                       ".center(columns) +bcolors.ENDC)
            print(bcolors.FAIL +f" [{bcolors.ENDC}2{bcolors.FAIL}].  Git clone                                    ".center(columns) +bcolors.ENDC)
            print(bcolors.FAIL +f" [{bcolors.ENDC}Q{bcolors.FAIL}].  Quit                                         ".center(columns) +bcolors.ENDC)
            print()
            value = input("Select: ")

            if value == "1":
                
                os.system("clear")
                os.system("cls")
                print(bcolors.FAIL + f"[{bcolors.ENDC}ERROR{bcolors.FAIL}] NOT WORKING".center(columns))
                input("Press any key to continue \n")
                loader(menu)

            elif value == "2":
                os.system("clear")
                os.system("cls")
                print(bcolors.FAIL + f"[{bcolors.ENDC}INFO{bcolors.FAIL}] Make sure you have git installed and a folder called 'UnnamedM' not exists.".center(columns) + bcolors.ENDC)
                print()
                input("Press any key to continue ")
            
                os.system("git clone https://github.com//HSp4m/UnnamedM")

                if os.path.isdir("UnnamedM\\"):
                    os.system("clear")
                    os.system("cls")
                    print(bcolors.OKGREEN + pyfiglet.figlet_format("OK", font='3d-ascii', justify="center"))

                    if os.path.isfile("UnnamedM\\unnamed.py"):
                        print(bcolors.ENDC + f"[{bcolors.OKBLUE}INFO{bcolors.ENDC}] Open 'UnnamedM\\unnamed.py' to start new version".center(columns) + bcolors.ENDC)
                        print()
                        exit()
                    else:
                        os.system("clear")
                        os.system("cls")
                        print(bcolors.FAIL + pyfiglet.figlet_format("ERROR", font='3d-ascii', justify="center").center(columns))
                        input("A error ocurred (File not found)." + bcolors.ENDC)
                        exit()
                else:
                    os.system("clear")
                    os.system("cls")
                    print(bcolors.FAIL + pyfiglet.figlet_format("ERROR", font='3d-ascii', justify="center").center(columns))
                    input("A error ocurred (Try to open file in powershell)." + bcolors.ENDC)
                    exit()
                
            elif value in ['q', 'Q']:
                os.system("clear")
                os.system("cls")
                exit()

        else:
            loader()
    else:
        os.system("clear")
        os.system("cls")
        
        print(bcolors.FAIL + pyfiglet.figlet_format("Updater", font='3d-ascii', justify="center").center(columns))
        print("Update Avaliable".center(columns))
        print()
        print(f"Script version: [{bcolors.ENDC}{c_version}{bcolors.FAIL}]".center(columns))
        print(f"Latest version: [{bcolors.ENDC}{u_version}{bcolors.FAIL}]".center(columns))
        print()

        value = input(f"{bcolors.ENDC}Update? [{bcolors.OKGREEN}Y{bcolors.ENDC}/{bcolors.FAIL}N{bcolors.ENDC}]: ")

        if value in ["N", "n"]:
            if os.path.isdir("UnnamedM\\"):
                if os.path.isfile("UnnamedM\\unnamed.py"):
                    os.system("clear")
                    os.system("cls")
                    print(bcolors.ENDC + f"[{bcolors.OKBLUE}INFO{bcolors.ENDC}] A possible updated file exist in 'UnnamedM\\unnamed.py'".center(columns))
                    print(bcolors.ENDC + f"[{bcolors.OKBLUE}INFO{bcolors.ENDC}] Delete folder if you want update again.".center(columns))
                    input("\nPress any key to continue \n")
                    exit()
            else:
                exit()
        elif value in ["S", "s", "Y", "y"]:
            if os.path.isdir("UnnamedM\\"):
                if os.path.isfile("UnnamedM\\unnamed.py"):
                    os.system("clear")
                    os.system("cls")
                    print(bcolors.ENDC + f"[{bcolors.OKBLUE}INFO{bcolors.ENDC}] A possible updated file exist in 'UnnamedM\\unnamed.py'".center(columns))
                    print(bcolors.ENDC + f"[{bcolors.OKBLUE}INFO{bcolors.ENDC}] Delete folder if you want update again.".center(columns))
                    input("\nPress any key to continue \n")
                    exit()
            
            os.system("clear")
            os.system("cls")
            print(bcolors.FAIL + pyfiglet.figlet_format("UP. Options", font='3d-ascii', justify="center").center(columns))
        
            print(bcolors.FAIL +f" [{bcolors.ENDC}1{bcolors.FAIL}].  Download (Not working)                       ".center(columns) +bcolors.ENDC)
            print(bcolors.FAIL +f" [{bcolors.ENDC}2{bcolors.FAIL}].  Git clone                                    ".center(columns) +bcolors.ENDC)
            print(bcolors.FAIL +f" [{bcolors.ENDC}Q{bcolors.FAIL}].  Quit                                         ".center(columns) +bcolors.ENDC)
            print()
            value = input("Select: ")

            if value == "1":
                
                os.system("clear")
                os.system("cls")
                print(bcolors.FAIL + f"[{bcolors.ENDC}ERROR{bcolors.FAIL}] NOT WORKING".center(columns))
                input("Press any key to continue \n")
                loader(menu)

            elif value == "2":
                os.system("clear")
                os.system("cls")
                print(bcolors.FAIL + f"[{bcolors.ENDC}INFO{bcolors.FAIL}] Make sure you have git installed and a folder called 'UnnamedM' not exists.".center(columns) + bcolors.ENDC)
                print()
                input("Press any key to continue ")
            
                os.system("git clone https://github.com//HSp4m/UnnamedM")

                if os.path.isdir("UnnamedM\\"):
                    os.system("clear")
                    os.system("cls")
                    print(bcolors.OKGREEN + pyfiglet.figlet_format("OK", font='3d-ascii', justify="center"))

                    if os.path.isfile("UnnamedM\\unnamed.py"):
                        print(bcolors.ENDC + f"[{bcolors.OKBLUE}INFO{bcolors.ENDC}] Open 'UnnamedM\\unnamed.py' to start new version".center(columns) + bcolors.ENDC)
                        print()
                        exit()
                    else:
                        os.system("clear")
                        os.system("cls")
                        print(bcolors.FAIL + pyfiglet.figlet_format("ERROR", font='3d-ascii', justify="center").center(columns))
                        input("A error ocurred (File not found)." + bcolors.ENDC)
                        exit()
                else:
                    os.system("clear")
                    os.system("cls")
                    print(bcolors.FAIL + pyfiglet.figlet_format("ERROR", font='3d-ascii', justify="center").center(columns))
                    input("A error ocurred (Try to open file in powershell)." + bcolors.ENDC)
                    exit()
                
            elif value in ['q', 'Q']:
                os.system("clear")
                os.system("cls")
                exit()
            
        else:
            loader()

if __name__ == "__main__":
    loader(menu)
