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
        input(f"Try: '{bcolors.ENDC}pip install pyfiglet{bcolors.FAIL}' and '{bcolors.ENDC}pip install requests{bcolors.FAIL}' \n")
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

url = 'https://raw.githubusercontent.com/HSp4m/UnnamedM/main/version.txt'
urlD = "https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/HSp4m/UnnamedM/blob/main/unnamed.py"
query_parameters = {"downloadformat": "py"}
page = urllib.request.urlopen(url)
c_version = "0.0.3"
u_version = f"{page.read()}".replace("b","").replace("'","").replace("n","").replace("\\","")
p_enabled = False;

def malwares():
    os.system("cls")
    print(bcolors.FAIL +"                                                                                                               ,;".center(columns))
    print("                                                i                                         j.                 f#i ".center(columns))
    print("          ..       :             ..            LE               ;                     ..  EW,              .E#t  ".center(columns))
    print("         ,W,     .Et            ;W,           L#E             .DL                    ;W,  E##j            i#W,   ".center(columns))
    print("        t##,    ,W#t           j##,          G#W.     f.     :K#L     LWL           j##,  E###D.         L#D.    ".center(columns))
    print("       L###,   j###t          G###,         D#K.      EW:   ;W##L   .E#f           G###,  E#jG#W;      :K#Wfff;  ".center(columns))
    print("     .E#j##,  G#fE#t        :E####,        E#K.       E#t  t#KE#L  ,W#;          :E####,  E#t t##f     i##WLLLLt ".center(columns))
    print("    ;WW; ##,:K#i E#t       ;W#DG##,      .E#E.        E#t f#D.L#L t#K:          ;W#DG##,  E#t  :K#E:    .E#L     ".center(columns))
    print("   j#E.  ##f#W,  E#t      j###DW##,     .K#E          E#jG#f  L#LL#G           j###DW##,  E#KDDDD###i     f#E:   ".center(columns))
    print(" .D#L    ###K:   E#t     G##i,,G##,    .K#D           E###;   L###j           G##i,,G##,  E#f,t#Wi,,,      ,WW;  ".center(columns))
    print(":K#t     ##D.    E#t   :K#K:   L##,   .W#G            E#K:    L#W;          :K#K:   L##,  E#t  ;#W:         .D#; ".center(columns))
    print("...      #G      ..   ;##D.    L##,  :W##########Wt   EG      LE.          ;##D.    L##,  DWi   ,KK:          tt ".center(columns))
    print("         j            ,,,      .,,   :,,,,,,,,,,,,,.  ;       ;@           ,,,      .,,                          ".center(columns))
    print()
    print("------------------------------------------------------------------------------------".center(columns))
    print()
    print(f"[{bcolors.ENDC}1{bcolors.FAIL}]. List Malwares".center(columns))
    print(f"[{bcolors.ENDC}Q{bcolors.FAIL}]. Quit".center(columns))
    print()
    value = input(bcolors.ENDC +"Select: ")

    if value in ["Q", "q"]:
        loader(menu)

def firewall():
    os.system("cls")
    print(bcolors.FAIL +"   ,                                                                                                           ".center(columns))
    print("   Et                                                                                                          ".center(columns))
    print("   E#t                                 ,;                                                                      ".center(columns))
    print("   E##t      t    j.                 f#i                                                  i                i   ".center(columns))
    print("   E#W#t     Ej   EW,              .E#t              ;                     ..            LE               LE   ".center(columns))
    print("   E#tfL.    E#,  E##j            i#W,             .DL                    ;W,           L#E              L#E   ".center(columns))
    print("   E#t       E#t  E###D.         L#D.      f.     :K#L     LWL           j##,          G#W.             G#W.   ".center(columns))
    print(",ffW#Dffj.   E#t  E#jG#W;      :K#Wfff;    EW:   ;W##L   .E#f           G###,         D#K.             D#K.    ".center(columns))
    print(" ;LW#ELLLf.  E#t  E#t t##f     i##WLLLLt   E#t  t#KE#L  ,W#;          :E####,        E#K.             E#K.     ".center(columns))
    print("   E#t       E#t  E#t  :K#E:    .E#L       E#t f#D.L#L t#K:          ;W#DG##,      .E#E.            .E#E.      ".center(columns))
    print("   E#t       E#t  E#KDDDD###i     f#E:     E#jG#f  L#LL#G           j###DW##,     .K#E             .K#E        ".center(columns))
    print("   E#t       E#t  E#f,t#Wi,,,      ,WW;    E###;   L###j           G##i,,G##,    .K#D             .K#D         ".center(columns))
    print("   E#t       E#t  E#t  ;#W:         .D#;   E#K:    L#W;          :K#K:   L##,   .W#G             .W#G          ".center(columns))
    print("   E#t       E#t  DWi   ,KK:          tt   EG      LE.          ;##D.    L##,  :W##########Wt   :W##########Wt ".center(columns))
    print("   ;#t       ,;.                           ;       ;@           ,,,      .,,   :,,,,,,,,,,,,,.  :,,,,,,,,,,,,,.".center(columns))
    print("    :;                                                                                                         ".center(columns))
    print()
    print()
    print("------------------------------------------------------------------------------------".center(columns))
    print()
    print(f"[{bcolors.ENDC}1{bcolors.FAIL}] Enable ".center(columns))
    print(f"[{bcolors.ENDC}2{bcolors.FAIL}] Disable ".center(columns))
    print(f"[{bcolors.ENDC}Q{bcolors.FAIL}] Quit ".center(columns))
    print()

    value = input(bcolors.ENDC + "Select: ")

    if value in ["Q", "q"]:
        loader(menu)

    elif value == "1":
        os.system("cls")

        os.system("netsh advfirewall set allprofiles state on")

        os.system("cls")

        print(f"[{bcolors.OKGREEN}ON{bcolors.ENDC}] Firewall".center(columns))

        time.sleep(5)
        loader(menu)

    elif value == "2":
        os.system("cls")

        os.system("netsh advfirewall set allprofiles state off")

        os.system("cls")

        print(f"[{bcolors.FAIL}OFF{bcolors.ENDC}] Firewall".center(columns))
        
        time.sleep(5)
        loader(menu)
    
def about():
    print(bcolors.FAIL +"                      .                       .                         ".center(columns))                         
    print(".    .               ;W  t                   ,W                         ".center(columns))                         
    print("Di   Dt             f#E  ED.                i##               ..       :".center(columns))
    print("E#i  E#i          .E#f   E#K:              f###              ,W,     .Et".center(columns))
    print("E#t  E#t         iWW;    E##W;            G####             t##,    ,W#t".center(columns))
    print("E#t  E#t        L##Lffi  E#E##t         .K#Ki##            L###,   j###t".center(columns))
    print("E########f.    tLLG##L   E#ti##f       ,W#D.,##          .E#j##,  G#fE#t".center(columns))
    print("E#j..K#j...      ,W#i    E#t ;##D.    i##E,,i##,        ;WW; ##,:K#i E#t".center(columns))
    print("E#t  E#t        j#E.     E#ELLE##K:  ;DDDDDDE##DGi     j#E.  ##f#W,  E#t".center(columns))
    print("E#t  E#t      .D#j       E#L;;;;;;,         ,##      .D#L    ###K:   E#t".center(columns))
    print("f#t  f#t     ,WK,        E#t                ,##     :K#t     ##D.    E#t".center(columns))
    print(" ii   ii     EG.         E#t                .E#     ...      #G      .. ".center(columns)) 
    print("             ,                                t              j          ".center(columns))
    print()
    print("------------------------------------------------------------------------------------".center(columns))
    print()  
    print("https://github.com/HSp4m".center(columns))
    print()
    print(f"Version: BETA {c_version}".center(columns))
    
    time.sleep(5)
    loader(menu)


def commands():
    
    os.system("cls")
    print(bcolors.FAIL +"                                                                                         ;                   ".center(columns))
    print("             :                                                                           ED.                 ".center(columns))
    print("      .,    t#,                                                           L.             E#Wi               .".center(columns))
    print("     ,Wt   ;##W.                                                          EW:        ,ft E###G.            ;W".center(columns))
    print("    i#D.  :#L:WE             ..       :           ..       :           .. E##;       t#E E#fD#W;          f#E".center(columns))
    print("   f#f   .KG  ,#D           ,W,     .Et          ,W,     .Et          ;W, E###t      t#E E#t t##L       .E#f ".center(columns))
    print(" .D#i    EE    ;#f         t##,    ,W#t         t##,    ,W#t         j##, E#fE#f     t#E E#t  .E#K,    iWW;  ".center(columns))
    print(":KW,    f#.     t#i       L###,   j###t        L###,   j###t        G###, E#t D#G    t#E E#t    j##f  L##Lffi".center(columns))
    print("t#f     :#G     GK      .E#j##,  G#fE#t      .E#j##,  G#fE#t      :E####, E#t  f#E.  t#E E#t    :E#K:tLLG##L ".center(columns))
    print(" ;#G     ;#L   LW.     ;WW; ##,:K#i E#t     ;WW; ##,:K#i E#t     ;W#DG##, E#t   t#K: t#E E#t   t##L    ,W#i  ".center(columns))
    print("  :KE.    t#f f#:     j#E.  ##f#W,  E#t    j#E.  ##f#W,  E#t    j###DW##, E#t    ;#W,t#E E#t .D#W;    j#E.   ".center(columns))
    print("   .DW:    f#D#;    .D#L    ###K:   E#t  .D#L    ###K:   E#t   G##i,,G##, E#t     :K#D#E E#tiW#G.   .D#j     ".center(columns))
    print("     L#,    G#t    :K#t     ##D.    E#t :K#t     ##D.    E#t :K#K:   L##, E#t      .E##E E#K##i    ,WK,      ".center(columns))
    print("      jt     t     ...      #G      ..  ...      #G      .. ;##D.    L##, ..         G#E E##D.     EG.       ".center(columns))
    print("                            j                    j          ,,,      .,,              fE E#t       ,         ".center(columns))
    print("                                                                                       , L:                  ".center(columns))
    print()
    print("------------------------------------------------------------------------------------".center(columns))
    print()
    print(f"[{bcolors.ENDC}1{bcolors.FAIL}]. Taskkill".center(columns))
    print(f"[{bcolors.ENDC}Q{bcolors.FAIL}]. Quit".center(columns))
    print()

    value = input("Select: ")

    if value in ["Q", "q"]:
        loader(menu)

def vrchat():
    print(bcolors.FAIL +"                                   .,                                  ".center(columns))
    print("           j.                     ,Wt .    .                           ".center(columns))
    print("           EW,                   i#D. Di   Dt              .. GEEEEEEEL".center(columns))
    print("t      .DD.E##j                 f#f   E#i  E#i            ;W, ,;;L#K;;.".center(columns))
    print("EK:   ,WK. E###D.             .D#i    E#t  E#t           j##,    t#E   ".center(columns))
    print("E#t  i#D   E#jG#W;           :KW,     E#t  E#t          G###,    t#E   ".center(columns))
    print("E#t j#f    E#t t##f          t#f      E########f.     :E####,    t#E   ".center(columns))
    print("E#tL#i     E#t  :K#E:         ;#G     E#j..K#j...    ;W#DG##,    t#E   ".center(columns))
    print("E#WW,      E#KDDDD###i         :KE.   E#t  E#t      j###DW##,    t#E   ".center(columns))
    print("E#K:       E#f,t#Wi,,,          .DW:  E#t  E#t     G##i,,G##,    t#E   ".center(columns))
    print("ED.        E#t  ;#W:              L#, f#t  f#t   :K#K:   L##,    t#E   ".center(columns))
    print("t          DWi   ,KK:              jt  ii   ii  ;##D.    L##,     fE   ".center(columns))
    print("                                                ,,,      .,,       :   ".center(columns))

    value = input("VRChat Folder: " + bcolors.ENDC)
    if os.path.isdir(value):
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
        os.system("cls")
        print(bcolors.FAIL +"                                           :                   ".center(columns))                  
        print("        ,;                                t#,                  ".center(columns))                 
        print("      f#i   j.           j.              ;##W.     j.          ".center(columns))         
        print("    .E#t    EW,          EW,            :#L:WE     EW,         ".center(columns))        
        print("   i#W,     E##j         E##j          .KG  ,#D    E##j        ".center(columns))       
        print("  L#D.      E###D.       E###D.        EE    ;#f   E###D.      ".center(columns))    
        print("i##WLLLLt   E#t t##f     E#t t##f     :#G     GK   E#t t##f    ".center(columns))   
        print(" .E#L       E#t  :K#E:   E#t  :K#E:    ;#L   LW.   E#t  :K#E:  ".center(columns)) 
        print("   f#E:     E#KDDDD###i  E#KDDDD###i    t#f f#:    E#KDDDD###i ".center(columns))
        print("    ,WW;    E#f,t#Wi,,,  E#f,t#Wi,,,     f#D#;     E#f,t#Wi,,, ".center(columns))
        print("     .D#;   E#t  ;#W:    E#t  ;#W:        G#t      E#t  ;#W:   ".center(columns))  
        print("       tt   DWi   ,KK:   DWi   ,KK:        t       DWi   ,KK:  ".center(columns))
        print()
        print("------------------------------------------------------------------------------------".center(columns))
        print()
        print(f"[{bcolors.ENDC}{value}{bcolors.FAIL}] it's not a valid folder.".center(columns))
        print()
        input("Press ANY key to continue.")
        print()
        menu()

def bruteforce():
    os.system("cls")
    print(bcolors.FAIL +f"                                                             {bcolors.ENDC},                                                ".center(columns))
    print(bcolors.FAIL +f"                                                             {bcolors.ENDC}Et           :                                   ".center(columns))
    print(bcolors.FAIL +f"                        :                        ,;          {bcolors.ENDC}E#t         t#,                     .,         ,;".center(columns))
    print(bcolors.FAIL +f".           j.          Ef                     f#i           {bcolors.ENDC}E##t       ;##W.   j.              ,Wt       f#i ".center(columns))
    print(bcolors.FAIL +f"Ef.         EW,         E#t     GEEEEEEEL    .E#t            {bcolors.ENDC}E#W#t     :#L:WE   EW,            i#D.     .E#t  ".center(columns))
    print(bcolors.FAIL +f"E#Wi        E##j        E#t     ,;;L#K;;.   i#W,             {bcolors.ENDC}E#tfL.   .KG  ,#D  E##j          f#f      i#W,   ".center(columns))
    print(bcolors.FAIL +f"E#K#D:      E###D.      E#t        t#E     L#D.              {bcolors.ENDC}E#t      EE    ;#f E###D.      .D#i      L#D.    ".center(columns))
    print(bcolors.FAIL +f"E#t,E#f.    E#jG#W;     E#t fi     t#E   :K#Wfff;         {bcolors.ENDC},ffW#Dffj. f#.     t#iE#jG#W;    :KW,     :K#Wfff;  ".center(columns))
    print(bcolors.FAIL +f"E#WEE##Wt   E#t t##f    E#t L#j    t#E   i##WLLLLt         {bcolors.ENDC};LW#ELLLf.:#G     GK E#t t##f   t#f      i##WLLLLt ".center(columns))
    print(bcolors.FAIL +f"E##Ei;;;;.  E#t  :K#E:  E#t L#L    t#E    .E#L               {bcolors.ENDC}E#t      ;#L   LW. E#t  :K#E:  ;#G      .E#L     ".center(columns))
    print(bcolors.FAIL +f"E#DWWt      E#KDDDD###i E#tf#E:    t#E      f#E:             {bcolors.ENDC}E#t       t#f f#:  E#KDDDD###i  :KE.      f#E:   ".center(columns))
    print(bcolors.FAIL +f"E#t f#K;    E#f,t#Wi,,, E###f      t#E       ,WW;            {bcolors.ENDC}E#t        f#D#;   E#f,t#Wi,,,   .DW:      ,WW;  ".center(columns))
    print(bcolors.FAIL +f"E#Dfff##E,  E#t  ;#W:   E#K,       t#E        .D#;           {bcolors.ENDC}E#t         G#t    E#t  ;#W:       L#,      .D#; ".center(columns))
    print(bcolors.FAIL +f"jLLLLLLLLL; DWi   ,KK:  EL          fE          tt           {bcolors.ENDC}E#t          t     DWi   ,KK:       jt        tt ".center(columns))
    print(bcolors.FAIL +f"                        :            :                       {bcolors.ENDC};#t                                              ".center(columns))
    print(bcolors.FAIL +f"                                                            {bcolors.ENDC}:;                                              ".center(columns) + bcolors.FAIL)
    print()
    print("------------------------------------------------------------------------------------".center(columns))
    print()
    print(f"[{bcolors.ENDC}1{bcolors.FAIL}]. WIFI bruteforce".center(columns))
    print(f"[{bcolors.ENDC}Q{bcolors.FAIL}]. Quit".center(columns))
    print()

    value = input(bcolors.ENDC + "Select: ")

    if value in ["Q", "q"]:
        loader(menu)

    elif value == "1":
        os.system("cls")

    
def menu():
    os.system("cls")
    print(bcolors.FAIL + pyfiglet.figlet_format("Crow 61", font='3d-ascii', justify="center"))
    print(bcolors.FAIL +f" [{bcolors.ENDC}1{bcolors.FAIL}].  Malwares                       ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +f" [{bcolors.ENDC}2{bcolors.FAIL}].  Windows Firewall               ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +f" [{bcolors.ENDC}3{bcolors.FAIL}].  BruteForce                     ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +f" [{bcolors.ENDC}4{bcolors.FAIL}].  VRChat [EAC Bypassed]          ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +f" [{bcolors.ENDC}5{bcolors.FAIL}].  Commands                       ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +f" [{bcolors.ENDC}9{bcolors.FAIL}].  About                          ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +f" [{bcolors.ENDC}Q{bcolors.FAIL}].  Quit                           ".center(columns) +bcolors.ENDC)
    print()
    print()

    value = input("Select: ")


    if value == "1" :
        os.system('cls')
        malwares()

    elif value == "2":
        firewall()

    elif value == "3":
        os.system('cls')
        bruteforce()

    elif value == "4":
        os.system('cls')
        vrchat()

    elif value == "5":
        os.system('cls')
        commands()

    elif value == "9":
        os.system('cls')
        
        about()

    elif value in ["Q", "q"]:
        exit()
    else:
        os.system("cls")
        print(bcolors.FAIL +"                                           :                   ".center(columns))                  
        print("        ,;                                t#,                  ".center(columns))                 
        print("      f#i   j.           j.              ;##W.     j.          ".center(columns))         
        print("    .E#t    EW,          EW,            :#L:WE     EW,         ".center(columns))        
        print("   i#W,     E##j         E##j          .KG  ,#D    E##j        ".center(columns))       
        print("  L#D.      E###D.       E###D.        EE    ;#f   E###D.      ".center(columns))    
        print("i##WLLLLt   E#t t##f     E#t t##f     :#G     GK   E#t t##f    ".center(columns))   
        print(" .E#L       E#t  :K#E:   E#t  :K#E:    ;#L   LW.   E#t  :K#E:  ".center(columns)) 
        print("   f#E:     E#KDDDD###i  E#KDDDD###i    t#f f#:    E#KDDDD###i ".center(columns))
        print("    ,WW;    E#f,t#Wi,,,  E#f,t#Wi,,,     f#D#;     E#f,t#Wi,,, ".center(columns))
        print("     .D#;   E#t  ;#W:    E#t  ;#W:        G#t      E#t  ;#W:   ".center(columns))  
        print("       tt   DWi   ,KK:   DWi   ,KK:        t       DWi   ,KK:  ".center(columns))
        print()
        print("------------------------------------------------------------------------------------".center(columns))
        print()
        print(f"[{bcolors.ENDC}{value}{bcolors.FAIL}] it's not valid.".center(columns))
        print()
        input("Press ANY key to continue.")
        print()
        menu()

page = urllib.request.urlopen(url)
u_version = f"{page.read()}".replace("b","").replace("'","").replace("n","").replace("\\","")

def loader(fnc):
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
            exit()
        elif value in ["S", "s", "Y", "y"]:
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
