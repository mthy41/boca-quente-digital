import getpass
from art import text2art
from colorama import *
#Incializar o colorama
init(autoreset=True)

from funs.tempdata import userlist, newsdict, comlist, data_import, data_export
from funs.clifun import horbar, verspace
from funs.siginfun import sigin
from funs.loggedfun import logged
from funs.recentnewsfun import recentnews
from funs.viewnewsfun import viewnews
from funs.addcomfun import addcom

data_import()
def main ():
    headerbq = text2art("Qb", "isometric3")
    while True:
        #test()
        print(f"{Fore.RED}{Style.BRIGHT}{headerbq}{Fore.RESET}{Style.RESET_ALL}\n")
        recentnews()
        menuchoice = str(input(
            "[1]Fazer login.\n"
            "[2]Cadastrar Leitor.\n"
            "[3]Cadastrar Editor.\n"
            "[4]Entrar como convidado.\n"
            "[0]Sair.\n"
            #f"{userlist}"
        ))
        #Sair
        if (menuchoice == "0"):
            data_export()
            break
        #Login
        if (menuchoice == "1"):
            while True:
                verspace()
                userinput = input("Digite seu usuário de login:\n>> ")
                upi = getpass.getpass("Digite sua senha:\n>> ")
                
                if (userinput in userlist):
                    #print("o usuario existe")
                    print(userlist[userinput][0])
                    if (upi == userlist[userinput][0]):
                        #print('a senha existe')
                        logged(userinput)
                        break
                    else:
                        print("Usuário não existe ou o senha está incorreta.\nPressione enter ou insira [0] para voltar ao início.")
                        c = input(">> ")
                        if (c == "0"):
                            break
                        else:
                            continue
                    
                else:
                    print("Usuário não existe ou o senha está incorreta.\nPressione enter ou insira [0] para voltar ao início.")
                    c = input(">> ")
                    if (c == "0"):
                        break
                    else:
                        continue
        #Login como convidado
        if (menuchoice == "4"):
            logged()
            
        #Cadastrar como leitor
        if (menuchoice == "2"):
            sigin("USER")
        if (menuchoice == "3"):
            sigin("ADM")
           

main()
