# IMPORTS
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

# IMPORTS VERIFY
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

atem = 0
guess = ''
url = 'https://raw.githubusercontent.com/HSp4m/UnnamedM/main/version.txt'
FileURL = 'https://raw.githubusercontent.com/HSp4m/UnnamedM/main/unnamed.py'

page = urllib.request.urlopen(url)
c_version = "0.1.1"
u_version = f"{page.read()}".replace("b","").replace("'","").replace("n","").replace("\\","")
p_enabled = False;

# CODE

class crackD:
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
                zip_file.close()
                input(": ")
                Loader.loader(Menu.menu)
                break;

            except:
                continue

    def crackP(zip_file, path, pathP):

        os.system("clear")
        os.system("cls")
        total = len(list(open(pathP,encoding='utf-8')))
        atem = 0
        crack = 0
        print(bcolors.FAIL + pyfiglet.figlet_format("Craking...", font='3d-ascii', width=110, justify="center"))
        print("------------------------------------------------------------------------------------".center(columns))
        print()
        print(f"[{bcolors.ENDC}*{bcolors.FAIL}] Trying '{total}' passwords.".center(columns))

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
                        
                        zip_file.close()
                        file.close()
                        input(": ")
                        Loader.loader(Menu.menu)
                        break;

                    except:

                        if total > 1000 and atem == 1000:
                            print()
                            print(f"{bcolors.FAIL}[{bcolors.ENDC}+{bcolors.FAIL}] {atem} Attempts!   ".center(columns))

                        if total > 10000 and atem == 10000:
                            print()
                            print(f"{bcolors.FAIL}[{bcolors.ENDC}+{bcolors.FAIL}] {atem} Attempts!   ".center(columns))
                        
                        if total > 100000 and atem == 100000:
                            print()
                            print(f"{bcolors.FAIL}[{bcolors.ENDC}+{bcolors.FAIL}] {atem} Attempts!   ".center(columns))

                        if total > 500000 and atem == 500000:
                            print()
                            print(f"{bcolors.FAIL}[{bcolors.ENDC}+{bcolors.FAIL}] {atem} Attempts!   ".center(columns))
                        
                        if total > 1000000 and atem == 1000000:
                            print()
                            print(f"{bcolors.FAIL}[{bcolors.ENDC}+{bcolors.FAIL}] {atem} Attempts!   ".center(columns))
                        
                        if total > 5000000 and atem == 5000000:
                            print()
                            print(f"{bcolors.FAIL}[{bcolors.ENDC}+{bcolors.FAIL}] {atem} Attempts!   ".center(columns))
                        
                        if total > 10000000 and atem == 10000000:
                            print()
                            print(f"{bcolors.FAIL}[{bcolors.ENDC}+{bcolors.FAIL}] {atem} Attempts!   ".center(columns))

                        

                        continue

        if atem == total:
            if crack == 0:
                os.system("clear")
                os.system("cls")
                print(bcolors.FAIL + pyfiglet.figlet_format("Not Found !", font='3d-ascii', width=110, justify="center"))
                print("------------------------------------------------------------------------------------".center(columns))
                print()
                print(f"Password not found in {atem} attempts".center(columns))
                input("\n: ")
                file.close()
                zip_file.close()
                Loader.loader(Menu.menu)
                



class Malwares:
    def malwaresMENU():
        os.system("clear")
        os.system("cls")
        print(bcolors.FAIL + pyfiglet.figlet_format("Malware", font='3d-ascii', width=110, justify="center"))
        print("------------------------------------------------------------------------------------".center(columns))
        print()
        print(f"[{bcolors.ENDC}01{bcolors.FAIL}]. List Malwares ".center(columns))
        print(f"[{bcolors.ENDC}00{bcolors.FAIL}]. Quit          ".center(columns))
        print()
        value = input(bcolors.ENDC +"Select: ")

        if value in ["0", "00"]:
            Loader.loader(Menu.menu)
        if value in ["1", "01"]:
            Malwares.listMALWARE()
        else:
            Loader.loader(Malwares.malwaresMENU)
        
    def listMALWARE():
        # soon
        os.system("clear")
        os.system("cls")
        print(bcolors.FAIL + pyfiglet.figlet_format("Malwares. List", font='3d-ascii', width=110, justify="center"))
        print("------------------------------------------------------------------------------------".center(columns))
        print()
        print(f"[{bcolors.ENDC}01{bcolors.FAIL}]. No malware found. (This option is in development)".center(columns))
        print(f"[{bcolors.ENDC}00{bcolors.FAIL}]. Quit                                             ".center(columns))
        print()
        value = input(bcolors.ENDC +"Select: ")

        if value in ["0", "00"]:
            Loader.loader(Menu.menu)

        elif value in ["1", "01"]:
            Loader.loader(Menu.menu)
        
        else:
            Loader.loader(Malwares.listMALWARE)

class Firewall:
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
            Loader.loader(Menu.menu)

        elif value in ["1", "01"]:
            os.system("clear")
            os.system("cls")

            os.system("netsh advfirewall set allprofiles state on")

            os.system("clear")
            os.system("cls")

            print(f"[{bcolors.OKGREEN}ON{bcolors.ENDC}] Firewall".center(columns))

            time.sleep(5)
            Loader.loader(Menu.menu)

        elif value in ["2", "02"]:
            os.system("clear")
            os.system("cls")

            os.system("netsh advfirewall set allprofiles state off")

            os.system("clear")
            os.system("cls")

            print(f"[{bcolors.FAIL}OFF{bcolors.ENDC}] Firewall".center(columns))
            
            time.sleep(5)
            Loader.loader(Menu.menu)
        else:
            Loader.loader(Firewall.firewall)
class About:
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
        Loader.loader(Menu.menu)

class Commands:
    def commandsList():
        os.system("clear")
        os.system("cls")
        print(bcolors.FAIL + pyfiglet.figlet_format("Commands", font='3d-ascii', width=110, justify="center"))
        print("------------------------------------------------------------------------------------".center(columns))
        print()
        print(f"[{bcolors.ENDC}01{bcolors.FAIL}]. Taskkill".center(columns))
        print(f"[{bcolors.ENDC}02{bcolors.FAIL}]. Faker   ".center(columns))
        print(f"[{bcolors.ENDC}00{bcolors.FAIL}]. Quit    ".center(columns))
        print()

        value = input("Select: ")

        if value in ["0", "00"]:
            Loader.loader(Menu.menu)

        if value in ["1", "01"]:
            Loader.loader(Commands.TASKKIL)
        
        if value in ["2", "02"]:
            Loader.loader(Commands.FAKER)
        
        else:
            Loader.loader(Commands.commandsList)
    
    def FAKER():
        os.system("clear")
        os.system("cls")

        print(bcolors.FAIL + pyfiglet.figlet_format("FAKER", font='3d-ascii', width=110, justify="center"))
        print("------------------------------------------------------------------------------------".center(columns))
        print()
        print(f"[{bcolors.ENDC}+{bcolors.FAIL}]. DISABLED.".center(columns))
        print()
        input()
        Loader.loader(Commands.commandsList)
    
    def TASKKIL():
        os.system("clear")
        os.system("cls")

        task = input("Task: ")
        print(bcolors.FAIL + pyfiglet.figlet_format("Taskkiller", font='3d-ascii', width=110, justify="center"))
        print("------------------------------------------------------------------------------------".center(columns))
        print()
        print(f"[{bcolors.ENDC}+{bcolors.FAIL}]. Selected Task: {task}".center(columns))
        print()
        input()
        Loader.loader(Commands.commandsList)

class passwords:
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
            Loader.loader(Menu.menu)

        elif value in ["1", "01"]:
            Loader.loader(passwords.WIFI)

        elif value in ["2", "02"]:
            Loader.loader(passwords.HASH)

        elif value in ["3", "03"]:
            Loader.loader(passwords.ZIP)
        
        else:
            Loader.loader(passwords.password)
            
    def WIFI():
        os.system("clear")
        os.system("cls")

        print(bcolors.FAIL + pyfiglet.figlet_format("WIFI BruteForce", font='3d-ascii', width=110, justify="center"))
        print("------------------------------------------------------------------------------------".center(columns))
        print()
        print(f"[{bcolors.ENDC}*{bcolors.FAIL}] SOON".center(columns))
        input()
        Loader.loader(passwords.password)
        
    def HASH():
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
            Loader.loader(Menu.menu)

        elif value in ["1", "01"]:
            Loader.loader(passwords.MD5)
                    

        elif value in ["2", "02"]:
            Loader.loader(passwords.SHA_256)

        elif value in ["3", "03"]:
            Loader.loader(passwords.SHA_1)
        
        else:
            Loader.loader(passwords.HASH)

    def MD5():
        os.system("clear")
        os.system("cls")
        print(bcolors.FAIL + pyfiglet.figlet_format("Hash. MD5", font='3d-ascii', width=110, justify="center"))
        print("------------------------------------------------------------------------------------".center(columns))
        print()
        value = input("Hash (MD5): ")
        valueF = input("Wordlist Path: ")

        if value != "" and os.path.isfile(valueF):
            os.system("clear")
            os.system("cls")
            print(bcolors.FAIL + pyfiglet.figlet_format("Cracking. Hash", font='3d-ascii', width=110, justify="center"))
            print("------------------------------------------------------------------------------------".center(columns))
            print()

            total = len(list(open(valueF,encoding='latin-1')))
            atem = 0
            crack = 0
            
            with open(valueF, "r", encoding="latin-1") as file:
                for line in file:
                    for password in line.split():
                        try:
                            atem += 1
                            passo = password.encode('utf-8')
                            digest = hashlib.md5(passo.strip()).hexdigest()
                            
                            if digest == value:
                                os.system("clear")
                                os.system("cls")
                                crack = 1
                                print(bcolors.OKGREEN + pyfiglet.figlet_format("Cracked !", font='3d-ascii', width=110, justify="center"))
                                print("------------------------------------------------------------------------------------".center(columns))
                                print()
                                print(f"Password: '{password}'.".center(columns))
                                file.close()
                                input("\n: ")
                                Loader.loader(Menu.menu)
                                break;

                        except:
                            continue;
                
            if atem == total and crack != 1:
                os.system("clear")
                os.system("cls")
                print(bcolors.FAIL + pyfiglet.figlet_format("Not found !", font='3d-ascii', width=110, justify="center"))
                print("------------------------------------------------------------------------------------".center(columns))
                print()
                print(f"Hash not found in wordlist. Total passwords: {atem}".center(columns))
                file.close()
                input("\n: ")
                Loader.loader(Menu.menu)
                

    def SHA_256():
        os.system("clear")
        os.system("cls")
        print(bcolors.FAIL + pyfiglet.figlet_format("Hash. SHA-256", font='3d-ascii', width=110, justify="center"))
        print("------------------------------------------------------------------------------------".center(columns))
        print()
        value = input("Hash (SHA-256): ")
        valueF = input("Wordlist Path: ")

        if value != "" and os.path.isfile(valueF):
            os.system("clear")
            os.system("cls")
            print(bcolors.FAIL + pyfiglet.figlet_format("Cracking. Hash", font='3d-ascii', width=110, justify="center"))
            print("------------------------------------------------------------------------------------".center(columns))
            print()

            total = len(list(open(valueF,encoding='latin-1')))
            atem = 0
            crack = 0

            with open(valueF, "r", encoding="latin-1") as file:
                for line in file:
                    for password in line.split():
                        try:
                            atem += 1
                            passo = password.encode('utf-8')
                            digest = hashlib.sha256(passo.strip()).hexdigest()
                            
                            if digest == value:
                                os.system("clear")
                                os.system("cls")
                                crack = 1
                                print(bcolors.OKGREEN + pyfiglet.figlet_format("Cracked !", font='3d-ascii', width=110, justify="center"))
                                print("------------------------------------------------------------------------------------".center(columns))
                                print()
                                print(f"Password: '{password}'.".center(columns))
                                file.close()
                                input("\n: ")
                                Loader.loader(Menu.menu)
                                break;

                        except:
                            continue;
                
            if atem == total and crack != 1:
                os.system("clear")
                os.system("cls")
                print(bcolors.FAIL + pyfiglet.figlet_format("Not found !", font='3d-ascii', width=110, justify="center"))
                print("------------------------------------------------------------------------------------".center(columns))
                print()
                print(f"Hash not found in wordlist. Total passwords: {atem}".center(columns))
                file.close()
                input("\n: ")
                Loader.loader(Menu.menu)
    
    def SHA_1():
        os.system("clear")
        os.system("cls")
        print(bcolors.FAIL + pyfiglet.figlet_format("Hash. SHA-1", font='3d-ascii', width=110, justify="center"))
        print("------------------------------------------------------------------------------------".center(columns))
        print()
        value = input("Hash (SHA-1): ")
        valueF = input("Wordlist Path: ")

        if value != "" and os.path.isfile(valueF):
            os.system("clear")
            os.system("cls")
            print(bcolors.FAIL + pyfiglet.figlet_format("Cracking. Hash", font='3d-ascii', width=110, justify="center"))
            print("------------------------------------------------------------------------------------".center(columns))
            print()

            total = len(list(open(valueF,encoding='latin-1')))
            atem = 0
            crack = 0

            with open(valueF, "r", encoding="latin-1") as file:
                for line in file:
                    for password in line.split():
                        try:
                            atem += 1
                            passo = password.encode('utf-8')
                            digest = hashlib.sha1(passo.strip()).hexdigest()
                            
                            if digest == value:
                                os.system("clear")
                                os.system("cls")
                                crack = 1
                                print(bcolors.OKGREEN + pyfiglet.figlet_format("Cracked !", font='3d-ascii', width=110, justify="center"))
                                print("------------------------------------------------------------------------------------".center(columns))
                                print()
                                print(f"Password: '{password}'.".center(columns))
                                file.close()
                                input("\n: ")
                                Loader.loader(Menu.menu)
                                break;

                        except:
                            continue;
                
            if atem == total and crack != 1:
                os.system("clear")
                os.system("cls")
                print(bcolors.FAIL + pyfiglet.figlet_format("Not found !", font='3d-ascii', width=110, justify="center"))
                print("------------------------------------------------------------------------------------".center(columns))
                print()
                print(f"Hash not found in wordlist. Total passwords: {atem}".center(columns))
                file.close()
                input("\n: ")
                Loader.loader(Menu.menu)

    def ZIP():
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
            verify = value.endswith(".zip")
            if os.path.isfile(value) and verify == True:
                value2 = input("\nPath to extract: ")

                if os.path.isdir(value2):
                    val = input("\nCharacters amount: ")
                    zip_value = zipfile.ZipFile(value, mode="r")
                    crackD.crack(zip_value,value2,val)

                else:
                    print(f"{bcolors.FAIL}[{bcolors.ENDC}ERROR{bcolors.FAIL}] Invalid Folder Path".center(columns))
                    input("\n:")
                    Loader.loader(passwords.password)

            else:
                print(f"{bcolors.FAIL}[{bcolors.ENDC}ERROR{bcolors.FAIL}] Invalid Zip Path".center(columns))
                input("\n:")
                Loader.loader(passwords.password)

        elif value in ["2", "02"]:

            os.system("clear")
            os.system("cls")

            print(bcolors.FAIL + pyfiglet.figlet_format("Zip. Cracker", font='3d-ascii', width=110, justify="center"))
            print("------------------------------------------------------------------------------------".center(columns))
            print()
            value = input(f" [{bcolors.ENDC}+{bcolors.FAIL}] Password list path: ")
            verify = False

            if os.path.isfile(value):
                value2 = input(f"\n [{bcolors.ENDC}+{bcolors.FAIL}] Zip Path: ")
                verify = value2.endswith(".zip")
                if os.path.isfile(value2) and verify == True:
                    value3 = input(f"\n [{bcolors.ENDC}+{bcolors.FAIL}] Path to extract: ")

                    if os.path.isdir(value3):
                        zip_file = zipfile.ZipFile(value2, mode="r")
                        crackD.crackP(zip_file,value3,value)

                    else:

                        print(f"{bcolors.FAIL}[{bcolors.ENDC}ERROR{bcolors.FAIL}] Invalid Folder Path".center(columns))
                        input("\n:")
                        Loader.loader(passwords.password)
                else:

                    print(f"{bcolors.FAIL}[{bcolors.ENDC}ERROR{bcolors.FAIL}] Invalid Zip Path".center(columns))
                    input("\n:")
                    Loader.loader(passwords.password)
            else:

                print(f"{bcolors.FAIL}[{bcolors.ENDC}ERROR{bcolors.FAIL}] Invalid Password list Path".center(columns))
                input("\n:")
                Loader.loader(passwords.password)

        elif value in ["0", "00"]:

            Loader.loader(Menu.menu)

        else:

            Loader.loader(passwords.password)
        
class Menu:    
    def menu():

        os.system("clear")
        os.system("cls")
        print(bcolors.FAIL + pyfiglet.figlet_format("Crow 61", font='3d-ascii', justify="center"))
        print(bcolors.FAIL +f" [{bcolors.ENDC}01{bcolors.FAIL}].  Malwares                       ".center(columns) +bcolors.ENDC)
        print(bcolors.FAIL +f" [{bcolors.ENDC}02{bcolors.FAIL}].  Windows Firewall               ".center(columns) +bcolors.ENDC)
        print(bcolors.FAIL +f" [{bcolors.ENDC}03{bcolors.FAIL}].  Passwords                      ".center(columns) +bcolors.ENDC)
        print(bcolors.FAIL +f" [{bcolors.ENDC}04{bcolors.FAIL}].  Commands                       ".center(columns) +bcolors.ENDC)
        print(bcolors.FAIL +f" [{bcolors.ENDC}99{bcolors.FAIL}].  About                          ".center(columns) +bcolors.ENDC)
        print(bcolors.FAIL +f" [{bcolors.ENDC}00{bcolors.FAIL}].  Quit                           ".center(columns) +bcolors.ENDC)
        print()
        print()

        value = input("Select: ")


        if value in  ["1", "01"] :
            os.system("clear")
            os.system("cls")
            Loader.loader(Malwares.malwaresMENU)

        elif value in  ["2", "02"]:
            Loader.loader(Firewall.firewall)

        elif value in  ["3", "03"]:
            os.system("clear")
            os.system("cls")
            Loader.loader(passwords.password)

        elif value in  ["4", "04"]:
            os.system("clear")
            os.system("cls")
            Loader.loader(Commands.commandsList)

        elif value == "99":
            os.system("clear")
            os.system("cls")
            
            Loader.loader(About.about)

        elif value in  ["0", "00"]:
            exit()

        else:
            os.system("clear")
            os.system("cls")
            print(f"[{bcolors.ENDC}{value}{bcolors.FAIL}] it's not a valid input.".center(columns))
            print()
            input("Press ANY key to continue.")
            print()
            Loader.loader(Menu.menu)

page = urllib.request.urlopen(url)
u_version = f"{page.read()}".replace("b","").replace("'","").replace("n","").replace("\\","")

class Loader:

    def loader(fnc):
        os.system("clear")
        os.system("cls")
        page = urllib.request.urlopen(url)
        u_version = f"{page.read()}".replace("b","").replace("'","").replace("n","").replace("\\","")
        if (u_version == c_version):
            fnc()

        elif (u_version < c_version):
            
            Loader.INVALID(fnc)

        else:
            Loader.UPDATE()


    def INVALID(fnc):
        print(bcolors.FAIL + pyfiglet.figlet_format("Updater", font='3d-ascii', justify="center").center(columns))
        print("Invalid version detected.".center(columns))
        print()
        print(f"Current version: [{bcolors.ENDC}{c_version}{bcolors.FAIL}]".center(columns))
        print(f"Latest version: [{bcolors.ENDC}{u_version}{bcolors.FAIL}]".center(columns))
        print()

        value = input(f"{bcolors.ENDC}Fix? [{bcolors.OKGREEN}Y{bcolors.ENDC}/{bcolors.FAIL}N{bcolors.ENDC}]: ")

        if value in ["N", "n"]:

            os.system("clear")
            os.system("cls")
            print(f"{bcolors.FAIL}[{bcolors.ENDC}!!{bcolors.FAIL}] Using invalid versions the script maybe not run.".center(columns))
            input("\n: ")
            fnc()
        elif value in ["S", "s", "Y", "y"]:
            Loader.DOWNLOAD()


    def UPDATE():
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
                    print(bcolors.ENDC + f"[{bcolors.OKBLUE}INFO{bcolors.ENDC}] Delete folder if you want to update again.".center(columns))
                    input("\nPress any key to continue \n")
                    exit()
            else:
                exit()
        elif value in ["S", "s", "Y", "y"]:
            Loader.DOWNLOAD()
    

    def DOWNLOAD():
        if os.path.isdir("UnnamedM\\"):
            if os.path.isfile("UnnamedM\\unnamed.py"):
                os.system("clear")
                os.system("cls")
                print(bcolors.ENDC + f"[{bcolors.OKBLUE}INFO{bcolors.ENDC}] A possible updated file exist in 'UnnamedM\\unnamed.py'".center(columns))
                print(bcolors.ENDC + f"[{bcolors.OKBLUE}INFO{bcolors.ENDC}] Delete folder if you want to update again.".center(columns))
                input("\nPress any key to continue \n")
                exit()
                
        os.system("clear")
        os.system("cls")
        print(bcolors.FAIL + pyfiglet.figlet_format("UP. Options", font='3d-ascii', justify="center").center(columns))
            
        print(bcolors.FAIL +f" [{bcolors.ENDC}01{bcolors.FAIL}].  Download                                     ".center(columns) +bcolors.ENDC)
        print(bcolors.FAIL +f" [{bcolors.ENDC}02{bcolors.FAIL}].  Git clone                                    ".center(columns) +bcolors.ENDC)
        print(bcolors.FAIL +f" [{bcolors.ENDC}00{bcolors.FAIL}].  Quit                                         ".center(columns) +bcolors.ENDC)
        print()
        value = input("Select: ")

        if value in ["1", "01"]:
                    
            os.system("clear")
            os.system("cls")
            print(bcolors.FAIL + f"[{bcolors.ENDC}*{bcolors.FAIL}] INSTALLING...".center(columns))
            try:
                
                newVersion = requests.get(f"{FileURL}")
                open("unnamed.py", "wb").write(newVersion.content)
                os.system("clear")
                os.system("cls")
                print(bcolors.OKGREEN + pyfiglet.figlet_format("OK", font='3d-ascii', justify="center"))
                print(f"{bcolors.FAIL}[{bcolors.ENDC}*{bcolors.FAIL}]{bcolors.WARNING} Execute 'Unnamed.py' again to complete update.".center(columns) + bcolors.ENDC)
                print()

            except NameError:
                os.system("clear")
                os.system("cls")
                print(bcolors.FAIL + pyfiglet.figlet_format("FAIL", font='3d-ascii', justify="center"))
                input(NameError)

        elif value in ["2", "02"]:
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
                input("A error ocurred (Try to open UNNAMED.py in powershell)." + bcolors.ENDC)
                exit()
                    
        elif value in ['0', '00']:
            os.system("clear")
            os.system("cls")
            exit()
                
        else:
            Loader.DOWNLOAD()

    
if __name__ == "__main__":
    Loader.loader(Menu.menu)
