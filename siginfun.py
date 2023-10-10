import getpass
from clifun import horbar, verspace
from tempdata import userlist, newsdict, comlist

def sigin():
    user = ""
    username = ""
    userage = ""
    userrole = ""
    userpassword = ""
    while True:
        verspace()
        print(
            f"Usuário: {user}\n"
            f"Nome completo: {username}\n"
            f"Idade: {userage}\n"
            #f"Cargo: {userrole}\n"
        )
        if (userrole == ""):
            print("Nessa plataforma, leitores podem visualizar, pesquisar e interagir com as notícias publicadas.\nJá os Editores, além de serem leitores, podem publicar e editar notícias.\n")
            userrolechoice = str(input("Você será leitor ou editor?\n[1]Leitor.\n[2]Editor.\n[0]Voltar ao menu principal.\n>> "))
            if (userrolechoice == "0"):
                break
            elif (userrolechoice == "1"):
                userrole = "USER"
                continue
            elif (userrolechoice == "2"):
                userrole = "ADM"
                continue
            else:
                input("Opção inválida. Pressione enter para continuar.\n>> ")
                userrole = ""
                continue
            
                
        if (user == ""):
            user = str(input("Insira o nome de usuário:\n>> "))
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
                userlist[len(userlist)+1] = [userpassword, username, userrole, []]
                break
            if (userrole == "ADM"):
                userlist[user] = [userpassword, username, userrole, [],[]]
                break               
