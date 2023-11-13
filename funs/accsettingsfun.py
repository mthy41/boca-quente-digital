from funs.clifun import *
from funs.tempdata import userlist
from colorama import Fore, Style
import getpass
#init(autoreset=True)

def usersettings(userinput):
    uservalues = userlist[userinput]
    useremail = uservalues[5]
    while True:
        verspace()

        #Esconder o email
        hiddenuseremail = ""
        for i in useremail:
            if (hiddenuseremail == ""):
                hiddenuseremail += i
            elif (len(hiddenuseremail) < len(useremail)-8):
                hiddenuseremail += "*"
            else:
                hiddenuseremail += i

        #Esconder a senha
        userpassword = uservalues[0]
        hiddenpassword = ""
        for i in userpassword:
            hiddenpassword += "*"

        #Informações da conta
        print(
            f"{horbar(20)}\n"
            f"{Style.BRIGHT}Informações da conta:{Style.RESET_ALL}\n\n"
            f"{Style.BRIGHT}Usuário de login:{Style.RESET_ALL} @{userinput}\n"
            f"{Style.BRIGHT}E-mail cadastrado:{Style.RESET_ALL} {hiddenuseremail}\n"
            f"{Style.BRIGHT}Nome cadastrado:{Style.RESET_ALL} {uservalues[1]}\n"
            f"{Style.BRIGHT}Senha cadastrada:{Style.RESET_ALL} {hiddenpassword}\n"
            f"{horbar(20)}"
        )

        #Painel de escolhas
        print(
            "[1]Mudar e-mail de cadastro.\n"
            "[2]Mudar usuário de login.\n"
            "[3]Mudar senha.\n"
            f"[4]{Fore.RED}{Style.BRIGHT}Desativar conta.{Fore.RESET}{Style.RESET_ALL}\n"
            "[0]Sair."
        )
        accuserchoice = input(">> ")
        
        #Escolhas
        
        #Sair
        if (accuserchoice == "0"):
            break
        
        #Mudar e-mai
        if (accuserchoice == "1"):
            useremail = str(input("Insira o novo e-mail:\n>> "))
            EmailChars = "@qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM.-_1234567890"
            EmailAllowedChars = []
            for aec in EmailChars:
                EmailAllowedChars.append(aec)
            #print (EmailAllowedChars)
            for i in useremail:
                if not i in EmailAllowedChars:
                    print("E-mail inserido inválido.")
                    input("Pressione enter para voltar.")
                    useremail = ""
                    break
            #if (useremail == ""):
            #    continue
            
            if useremail.count("@") == 0 or useremail.count("@") > 1:
                print("E-mail inserido inválido.")
                input("Pressione enter para voltar.")
                #useremail = ""
                continue
            topleveldomaincheck = []
            for i in useremail:
                topleveldomaincheck.append(i)
            topleveldomaincheck.reverse()
            #print(topleveldomaincheck)
            if (topleveldomaincheck[0] != "m"):
                print("E-mail inserido inválido.")
                input("Pressione enter para voltar.")
                #useremail = ""
                continue
            if (topleveldomaincheck[1] != "o"):
                print("E-mail inserido inválido.")
                input("Pressione enter para voltar.")
                #useremail = ""
                continue
            if (topleveldomaincheck[2] != "c"):
                print("E-mail inserido inválido.")
                input("Pressione enter para voltar.")
                #useremail = ""
                continue
            if (topleveldomaincheck[3] != "."):
                print("E-mail inserido inválido.")
                input("Pressione enter para voltar.")
                #useremail = ""
                continue
            #emailusagecheck = []
            for i in userlist:
                checkUserValues = userlist[i]
                if (i == userinput):
                    continue
                if (useremail in checkUserValues):
                    print("E-mail inserido já está em uso.")
                    input("Pressione enter para voltar.")
                    #useremail = ""
                    continue
            passcheck = getpass.getpass("Digite sua senha para confirmar alteração.")
            if (passcheck != uservalues[0]):
                print("Senha incorreta.")
                input("Pressione enter para continuar.")
                useremail = uservalues[5]
            else:
                uservalues[5] = useremail
                userlist[userinput] = uservalues
            continue
        
        #mudar usuario
        if (accuserchoice == "2"):
            userChars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_1234567890"
            userAllowedChars = []
            for aec in userChars:
                userAllowedChars.append(aec)
            #print (userAllowedChars)
            user = str(input("Insira o nome de usuário de login:\n>> "))
            
            for i in user:
                if not i in userAllowedChars:
                    print("Usuário de login com caractere(s) inválido(s)")
                    input("Pressione enter para voltar.")
                    break            
            if (user in userlist):
                print("O usuário inserido já está em uso.")
                input("Pressione enter para continuar.")
                continue
            continue #

