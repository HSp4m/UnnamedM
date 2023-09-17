import requests
import shutil
import os
import time
import subprocess
import urllib.request
import re
import pyfiglet

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
c_version = "0.0.1"
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

def payloader():
    os.system("cls")
    if (p_enabled == False):
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
        print(f"{bcolors.FAIL} This option is disabled.".center(columns))
        print()
        input("Press ANY key to continue.")
        print()
        menu()

def menu():
    os.system("cls")
    print(bcolors.FAIL +"                                                                                 ;           ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +"                                                                                 ED.         ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +":      L.             L.                                                        ,E#Wi        ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +"Ef     EW:        ,ft EW:        ,ft                                          f#iE###G.      ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +"E#t    E##;       t#E E##;       t#E            ..           ..       :     .E#t E#fD#W;     ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +"E#t    E###t      t#E E###t      t#E           ;W,          ,W,     .Et    i#W,  E#t t##L    ".center(columns) +bcolors.ENDC) 
    print(bcolors.FAIL +"E#t    E#fE#f     t#E E#fE#f     t#E          j##,         t##,    ,W#t   L#D.   E#t  .E#K,  ".center(columns) +bcolors.ENDC) 
    print(bcolors.FAIL +"E#t fi E#t D#G    t#E E#t D#G    t#E         G###,        L###,   j###t :K#Wfff; E#t    j##f ".center(columns) +bcolors.ENDC) 
    print(bcolors.FAIL +"E#t L#jE#t  f#E.  t#E E#t  f#E.  t#E       :E####,      .E#j##,  G#fE#t i##WLLLLtE#t    :E#K:".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +"E#t L#LE#t   t#K: t#E E#t   t#K: t#E      ;W#DG##,     ;WW; ##,:K#i E#t  .E#L    E#t   t##L  ".center(columns) +bcolors.ENDC)  
    print(bcolors.FAIL +"E#tf#E:E#t    ;#W,t#E E#t    ;#W,t#E     j###DW##,    j#E.  ##f#W,  E#t    f#E:  E#t .D#W;   ".center(columns) +bcolors.ENDC)    
    print(bcolors.FAIL +"E###f  E#t     :K#D#E E#t     :K#D#E    G##i,,G##,  .D#L    ###K:   E#t     ,WW; E#tiW#G.    ".center(columns) +bcolors.ENDC)    
    print(bcolors.FAIL +"E#K,   E#t      .E##E E#t      .E##E  :K#K:   L##, :K#t     ##D.    E#t      .D#;E#K##i      ".center(columns) +bcolors.ENDC)      
    print(bcolors.FAIL +"EL     ..         G#E ..         G#E ;##D.    L##, ...      #G      ..         ttE##D.       ".center(columns) +bcolors.ENDC)       
    print(bcolors.FAIL +":                  fE             fE ,,,      .,,           j                    E#t         ".center(columns) +bcolors.ENDC)        
    print(bcolors.FAIL +"                    ,              ,                                             L:          ".center(columns) +bcolors.ENDC)
    print()
    print()
    print()
    print(bcolors.FAIL +f" [{bcolors.ENDC}1{bcolors.FAIL}].  Malwares                       ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +f" [{bcolors.ENDC}2{bcolors.FAIL}].  Windows Firewall               ".center(columns) +bcolors.ENDC)
    print(bcolors.FAIL +f" [{bcolors.ENDC}3{bcolors.FAIL}].  PayLoader                      ".center(columns) +bcolors.ENDC)
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
        payloader()

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

def loader(fnc):
    os.system("cls")
    if (u_version == c_version):
        
        fnc()
    elif (u_version < c_version):
        print(bcolors.FAIL +"                     ;                                                              ".center(columns))
        print("                     ED.                                                            ".center(columns))
        print(":                    E#Wi                                            ,;             ".center(columns))
        print("Ef       t           E###G.                                        f#i   j.         ".center(columns))
        print("E#t      ED.         E#fD#W;                  ..  GEEEEEEEL      .E#t    EW,        ".center(columns))
        print("E#t      E#K:        E#t t##L                ;W,  ,;;L#K;;.     i#W,     E##j       ".center(columns))
        print("E#t      E##W;       E#t  .E#K,             j##,     t#E       L#D.      E###D.     ".center(columns))
        print("E#t fi   E#E##t      E#t    j##f           G###,     t#E     :K#Wfff;    E#jG#W;    ".center(columns))
        print("E#t L#j  E#ti##f     E#t    :E#K:        :E####,     t#E     i##WLLLLt   E#t t##f   ".center(columns))
        print("E#t L#L  E#t ;##D.   E#t   t##L         ;W#DG##,     t#E      .E#L       E#t  :K#E: ".center(columns))
        print("E#tf#E:  E#ELLE##K:  E#t .D#W;         j###DW##,     t#E        f#E:     E#KDDDD###i".center(columns))
        print("E###f    E#L;;;;;;,  E#tiW#G.         G##i,,G##,     t#E         ,WW;    E#f,t#Wi,,,".center(columns))
        print("E#K,     E#t         E#K##i         :K#K:   L##,     t#E          .D#;   E#t  ;#W:  ".center(columns))
        print("EL       E#t         E##D.         ;##D.    L##,      fE            tt   DWi   ,KK: ".center(columns))
        print(":                    E#t           ,,,      .,,        :                            ".center(columns))
        print("                     L:                                                             ".center(columns))
        print()
        print("------------------------------------------------------------------------------------".center(columns))
        print()
        print("Invalid version detected.".center(columns))
        print()
        print(f"Current version: [{bcolors.ENDC}{c_version}{bcolors.FAIL}]".center(columns))
        print(f"Latest version: [{bcolors.ENDC}{u_version}{bcolors.FAIL}]".center(columns))
        print()

        value = input(f"{bcolors.ENDC}Fix? [{bcolors.OKGREEN}Y{bcolors.ENDC}/{bcolors.FAIL}N{bcolors.ENDC}]: ")

        if value in ["N", "n"]:
            fnc()
        elif value in ["S", "s", "Y", "y"]:
            newVersion = requests.get(f"{urlD}", params=query_parameters)
            open("unnamed.py", "wb").write(newVersion.content)
            os.system("cls")
            print(bcolors.OKGREEN +"[UPDATE] OK (Start script again)".center(columns))
            exit()
        else:
            loader()
    else:
        
        print(bcolors.FAIL +"                     ;                                                              ".center(columns))
        print("                     ED.                                                            ".center(columns))
        print(":                    E#Wi                                            ,;             ".center(columns))
        print("Ef       t           E###G.                                        f#i   j.         ".center(columns))
        print("E#t      ED.         E#fD#W;                  ..  GEEEEEEEL      .E#t    EW,        ".center(columns))
        print("E#t      E#K:        E#t t##L                ;W,  ,;;L#K;;.     i#W,     E##j       ".center(columns))
        print("E#t      E##W;       E#t  .E#K,             j##,     t#E       L#D.      E###D.     ".center(columns))
        print("E#t fi   E#E##t      E#t    j##f           G###,     t#E     :K#Wfff;    E#jG#W;    ".center(columns))
        print("E#t L#j  E#ti##f     E#t    :E#K:        :E####,     t#E     i##WLLLLt   E#t t##f   ".center(columns))
        print("E#t L#L  E#t ;##D.   E#t   t##L         ;W#DG##,     t#E      .E#L       E#t  :K#E: ".center(columns))
        print("E#tf#E:  E#ELLE##K:  E#t .D#W;         j###DW##,     t#E        f#E:     E#KDDDD###i".center(columns))
        print("E###f    E#L;;;;;;,  E#tiW#G.         G##i,,G##,     t#E         ,WW;    E#f,t#Wi,,,".center(columns))
        print("E#K,     E#t         E#K##i         :K#K:   L##,     t#E          .D#;   E#t  ;#W:  ".center(columns))
        print("EL       E#t         E##D.         ;##D.    L##,      fE            tt   DWi   ,KK: ".center(columns))
        print(":                    E#t           ,,,      .,,        :                            ".center(columns))
        print("                     L:                                                             ".center(columns))
        print()
        print("------------------------------------------------------------------------------------".center(columns))
        print()
        print("Update Avaliable".center(columns))
        print()
        print(f"Script version: [{bcolors.ENDC}{c_version}{bcolors.FAIL}]".center(columns))
        print(f"Latest version: [{bcolors.ENDC}{u_version}{bcolors.FAIL}]".center(columns))
        print()

        value = input(f"{bcolors.ENDC}Update? [{bcolors.OKGREEN}Y{bcolors.ENDC}/{bcolors.FAIL}N{bcolors.ENDC}]: ")

        if value in ["N", "n"]:
            exit()
        elif value in ["S", "s", "Y", "y"]:
            newVersion = requests.get(f"{urlD}", params=query_parameters)
            open("unnamed.py", "wb").write(newVersion.content)
            print(bcolors.OKGREEN +"[UPDATE] OK (Start script again)".center(columns))
            exit()
            
        else:
            loader()

if __name__ == "__main__":
    loader(menu)
