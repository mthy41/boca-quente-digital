import getpass

from tempdata import userlist, newsdict, comlist
from clifun import horbar, verspace
from siginfun import sigin
from loggedfun import logged
from recentnewsfun import recentnews
from viewnewsfun import viewnews
from addcomfun import addcom

def main ():
    while True:
        recentnews()
        print("Bem vindo, selecione sua opção:")
        menuchoice = str(input(
            "[1]Fazer login.\n"
            "[2]Cadastrar.\n"
            "[3]Entrar como convidado.\n"
            "[0]Sair.\n"
            #f"{userlist}"
        ))
        #Sair
        if (menuchoice == "0"):
            break
        #Login
        if (menuchoice == "1"):
            while True:
                verspace()
                userinput = input("Digite seu usuário de login:\n>> ")
                upi = getpass.getpass("Digite sua senha:\n>> ")
                
                if (userinput in userlist):
                    #print("o usuario existe")
                    if (upi in userlist[userinput][0]):
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
        if (menuchoice == "3"):
            logged()
            
        if (menuchoice == "2"):
            sigin()
            
main()