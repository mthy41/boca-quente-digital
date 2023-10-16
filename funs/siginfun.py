import getpass

from funs.clifun import horbar, verspace
from funs.tempdata import userlist, newsdict, comlist, data_import, data_export

def sigin(userrole):
    user = ""
    username = ""
    userage = ""
    useremail = ""
    #userrole = ""
    userpassword = ""
    while True:
        verspace()
        print(
            f"E-mail: {useremail}\n"
            f"Login: {user}\n"
            f"Nome completo: {username}\n"
            f"Idade: {userage}\n"
            #f"Cargo: {userrole}\n"
        )
        #if (userrole == ""):
        #    print("Nessa plataforma, leitores podem visualizar, pesquisar e interagir com as notícias publicadas.\nJá os Editores, além de serem leitores, podem publicar e editar notícias.\n")
        #    userrolechoice = str(input("Você será leitor ou editor?\n[1]Leitor.\n[2]Editor.\n[0]Voltar ao menu principal.\n>> "))
        #    if (userrolechoice == "0"):
        #        break
        #    elif (userrolechoice == "1"):
        #        userrole = "USER"
        #        continue
        #    elif (userrolechoice == "2"):
        #        userrole = "ADM"
        #        continue
        #    else:
        #        input("Opção inválida. Pressione enter para continuar.\n>> ")
        #        userrole = ""
        #        continue
            
        
        if (useremail == ""):
            useremail = str(input("Insira seu e-mail:\n>> "))
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
            if (useremail == ""):
                continue
            
            if useremail.count("@") == 0 or useremail.count("@") > 1:
                print("E-mail inserido inválido.")
                input("Pressione enter para voltar.")
                useremail = ""
                continue

            topleveldomaincheck = []
            for i in useremail:
                topleveldomaincheck.append(i)
            topleveldomaincheck.reverse()
            #print(topleveldomaincheck)
            if (topleveldomaincheck[0] != "m"):
                print("E-mail inserido inválido.")
                input("Pressione enter para voltar.")
                useremail = ""
                continue
            if (topleveldomaincheck[1] != "o"):
                print("E-mail inserido inválido.")
                input("Pressione enter para voltar.")
                useremail = ""
                continue
            if (topleveldomaincheck[2] != "c"):
                print("E-mail inserido inválido.")
                input("Pressione enter para voltar.")
                useremail = ""
                continue
            if (topleveldomaincheck[3] != "."):
                print("E-mail inserido inválido.")
                input("Pressione enter para voltar.")
                useremail = ""
                continue
                
            #emailusagecheck = []
            for i in userlist:
                uservalues = userlist[i]
                if (useremail in uservalues):
                    print("E-mail inserido já está em uso.")
                    input("Pressione enter para voltar.")
                    useremail = ""
                    continue
            continue
        
        if (user == ""):
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
                    user = ""
                    break            
            if (user in userlist):
                print("O usuário inserido já está em uso.")
                user = ""
                input("Pressione enter para continuar.")
                continue
            continue #
        if (username == ""):
            firstusername = str(input("Insira o seu primeiro nome:\n>> "))
            if (firstusername == "" or len(firstusername) <= 2):
                print("Primeiro nome inválido. Pressione enter para continaur.")
                input()
                continue
            lastusername = str(input("Insira o seu sobrenome:\n>> "))
            if (lastusername == "" or len(lastusername) == 2):
                print("Primeiro nome inválido. Pressione enter para continaur.")
                input()
                continue
            username = firstusername.capitalize() + " " + lastusername.capitalize()
            continue
        if (userage == ""):
            userage = input("Insira a sua idade:\n>> ")
            try:
                userage = int(userage)
            except ValueError:
                print("Idade inválida. Pressione enter para continuar.")
                input()
                userage = ""
                continue
            if (userage < 18):
                print("Você não tem idade suficiente para fazer uma conta.")
                input(">> ")
                break
            continue
        
        if (userpassword == ""):
            passwordone = getpass.getpass("Insira uma nova senha.\n>> ")
            if len(passwordone) <= 5:
                input("Sua senha precisa ter pelo menos 6 caracteres.\nPressione enter para continuar.\n>> ")
                continue
            for i in passwordone:
                if (i == " "):
                    print("Sua senha não pode conter espaços.")
                    input("Pressione enter para continuar.")
                    passwordone = ""
                    break
            if (passwordone == ""):
                continue
            passwordtwo = getpass.getpass("Verifique a senha.\n>> ")
            if (passwordone != passwordtwo):
                input("Senhas não batem.\nPressione enter para continuar.\n>> ")
                continue
            userpassword = passwordone
            continue
                
                        
        signinchoice = input(
            "[1]Confirmar cadastro.\n"
            "[0]Cancelar e sair.\n"
        )
        if (signinchoice == "0"):
            break
        if (signinchoice == "1"):
#"guest": ["guest", "convidado", "GUEST",[]]
            if (userrole == "USER"):
                userlist[user] = [userpassword, username, userrole, [], useremail]
                data_export()
                break
            if (userrole == "ADM"):
                userlist[user] = [userpassword, username, userrole, [],[], useremail]
                data_export()
                break               
