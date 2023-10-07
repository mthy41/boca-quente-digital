import getpass
import datetime


#Estrutura de dados:
#"user":["senha", "nome completo", "cargo", [ids de noticias publicadas]]
#o [ids de noticias publicadas] apenas para usuarios do cargo ADM

userlist = {
    "guest": ["guest", "convidado", "GUEST"],
    "cat": ["123", "Miguel Ohara", "ADM", []],
    "rat":["123", "Kimberlie Schwatson", "USER"],
    "dog":["123", "Miles Morales", "USER"],
    "bird":["123", "Ivan Neves", "USER"]
}

newsdict = {}

comlist = {
    "comID":["comAuthor", "comText"]
}

def dateandtime ():
    now = datetime.datetime.now()
    format = "%Y-%m-%d %H:%M:%S"
    currentTime = now.strftime(format)
    return(currentTime)
    

def postnew (userinput):
    title = str(input("Insira o título:\n>> "))
    body = str(input("Insira o texto:\n>> "))
    while True:
        print(
            f"Título: {title}\n"
            f"Texto: {body}\n"
            "[1]Adicionar ou editar título.\n"
            "[2]Adicionar ou editar texto.\n"
            "[3]Publicar.\n"
            "[0]Sair.\n"
        )
        #Voltar
        userchoicepostnew = str(input())
        if (userchoicepostnew == "0"):
            while True:
                userchoicesure = str(input("Deseja sair sem salvar? [0] para sim ou [1] para cancelar.\n>> "))
                if (userchoicesure == "0"):
                    break
                elif (userchoicesure == "1"):
                    break
                else:
                    print("Opção inválida.")
                    continue
            if (userchoicesure == "1"):
                continue
            break

        #Add titulo
        if (userchoicepostnew == "1"):
            title = str(input("Insira o novo título:\n>> "))

        #Add texto
        if (userchoicepostnew == "2"):
            body = str(input("Insira o novo texto:\n>> "))

        #Publicar
        if (userchoicepostnew == "3"):
            newsid = str(len(newsdict) + 1)
            newsvalues = [title, body, (userlist[userinput][1]),(dateandtime()), []]
            newsdict[newsid] = newsvalues
            print(newsdict)


def logged (userinput="guest"):
    while True:
        print (f"Bem vindo(a) {userlist[userinput][1]}")
        print(
            "[0]Deslogar.\n"
            "[1]Pesquisar notícias.\n"
            "[2]Listar notícias."
        )
        
        if userlist[userinput][2] == "USER":
            print(
                "[3]Configurações da conta."
            )
        
        if userlist[userinput][2] == "ADM":
            print(
                "[3]Configurações da conta.\n"
                "[4]Publicar notícia.\n"
                "[5]Editar notícia.\n"
                "[6]Excluir notícia.\n"

            )
        #Choices
        userloggedchoice = str(input(">> "))
        if (userloggedchoice == "0"):
            break
        
        if userlist[userinput][2] == "ADM":
            if (userloggedchoice == "4"):
                postnew(userinput)


def main ():
    while True:
        print("Menu\nBem vindo, selecione sua opção:")
        menuchoice = str(input(
            "[1]Fazer login.\n"
            "[2]Cadastrar.\n"
            "[3]Entrar como convidado.\n"
            "[0]Sair.\n"
        ))
        #Sair
        if (menuchoice == "0"):
            break
        #Login
        if (menuchoice == "1"):
            while True:
                userinput = input("Digite seu usuário de login:\n>> ")
                upi = getpass.getpass("Digite sua senha:\n>> ")
                
                if (userinput in userlist):
                    print("o usuario existe")
                    if (upi in userlist[userinput][0]):
                        print('a senha existe')
                        logged(userinput)
                        break
                    else:
                        print('A senha digitada está incorreta. Tente novamente.')
                        continue
                    
                else:
                    print("O login não existe ou o usuário está incorreto. Tente novamente.")
                    continue
        #Login como convidado
        if (menuchoice == "3"):
            logged()
            

main()