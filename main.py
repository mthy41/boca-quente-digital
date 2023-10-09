import getpass
import datetime


#Estrutura de dados:
#"user":["senha", "nome completo", "cargo", [ids de noticias curtidas], [ids de noticias publicadas]]
#o [ids de noticias publicadas] apenas para usuarios do cargo ADM

userlist = {
    "guest": ["guest", "convidado", "GUEST",[]],
    "cat": ["123", "Miguel Ohara", "ADM", [],[]],
    "rat":["123", "Kimberlie Schwatson", "USER",[]],
    "dog":["123", "Miles Morales", "USER", []],
    "bird":["123", "Ivan Neves", "USER",[]]
}

newsdict = {
    "1": ["title", "body", "author", "date", 3, []],
    "2": ["title2", "body2", "author2", "date2", 5, ["1", "2"]],
    "3": ["title3", "body3", "author3", "date3", 1, []]
}

comlist = {
    #"id do comentario":["id da noticia comentada", "user que comentou", "comentário"]
    "1":["2", "comAuthor", "comText"],
    "2":["2", "dog", "que bosta de noticia"]
}

def horbar (horbar):
    bar = "―"*45
    return bar

def verspace ():
    print("\n"*50)

def dateandtime ():
    now = datetime.datetime.now()
    format = "%Y-%m-%d %H:%M:%S"
    currentTime = now.strftime(format)
    return(currentTime)


def addcom (userinput, userchoice, uservalues, newsvalues):
    verspace()
    com = str(input(
        "Insira seu comentário:\n>> "
    ))
    print(horbar(horbar))
    print(com)
    print(horbar(horbar))
    print(
        "Publicar comentário?\n"
        "[1]Sim.\n"
        "[0]Não."
    )
    comconfirm = input(">> ")
    if (comconfirm == "1"):
        comvalues = [userchoice, userinput, com]
        comlist[str(len(comlist)+1)] = comvalues
        newsvalues[5].append(str(len(comlist)))
    else:
        print("Operação cancelada.")


def viewcom (userinput, uservalues, userchoice):
    while True:
        verspace()
        newsvalues = newsdict[userchoice]
        for i in (newsvalues[5]):
            comvalues = comlist[i]
            print(f"@{comvalues[1]}: {comvalues[2]}")
            print(horbar(horbar))
        
        print(
            "[0]Sair."
        )
        if uservalues[2] == "USER" or uservalues[2] == "ADM":
            print(
            "[1]Adicionar comentário.\n"
            )
            
        userviewcomchoice = input("")
        
        #Sair
        if (userviewcomchoice == "0"):
            break
        
        #Adicionar comentário
        if (uservalues[2] != "GUEST"):
            if (userviewcomchoice == "1"):
                addcom(userinput, uservalues, userchoice, newsvalues)
                #break
            
        

def viewnews (userinput, userchoice):
    newsvalues = newsdict[userchoice]
    uservalues = userlist[userinput]
    likedNewsIDs = uservalues[3]
    isliked = False
    while True:
        verspace()
        if userchoice in likedNewsIDs:
            isliked = True
            likeopt = "[1]Remover curtida."
        else:
            isliked = False
            likeopt = "[1]Curtir notícia."
        print(
            #f"{likedNewsIDs}\n"
            f"{newsvalues[0]}\n" #Tutulo
            f"{newsvalues[1]}\n" #Texto
            f" ❤ {newsvalues[4]} | Publicado por @{newsvalues[2]} | {newsvalues[3]}\n" #Curtidas, Autor, Data
            f"{horbar(horbar)}\n"
            f"{likeopt}\n"
            "[2]Comentar na notícia.\n"
            "[3]Ver comentários\n"
            "[0]Sair."
        )
        userviewchoice = str(input(">> "))
        
        #Curtir ou remover curtida
        if (userviewchoice == "1"):
            if (isliked == False):
                (likedNewsIDs.append(userchoice))
                uservalues.insert(3,likedNewsIDs)
                newsvalues[4] += 1
                #isliked = True
                continue
            if (isliked == True):
                likedNewsIDs = uservalues[3]
                likedNewsIDs.remove(userchoice)
                uservalues.insert(3, likedNewsIDs)
                newsvalues[4] -= 1
                continue
        #Sair
        if (userviewchoice == "0"):
            newsdict[userchoice] = newsvalues
            userlist[userinput] = uservalues
            break
        
        #Comentar na notícia
        if (userviewchoice == "2"):
            if (uservalues[2] == "GUEST"):
                print("Você precisa fazer login para poder comentar.")
                input("Pressione enter para voltar.")
            else:
                addcom(userinput, userchoice, uservalues, newsvalues)
        
        #Ver comentarios
        if (userviewchoice == "3"):
            viewcom(userinput, uservalues, userchoice)


def listnews (userinput):
    islistreversed = False #Ordem padrão (das mais velhas as mais novas)
    while True:
        verspace()
        if (islistreversed == False):
            for i in range (1, (len(newsdict) + 1)):
                newsvalues = newsdict[str(i)]
                print(
                    f"ID[{i}] {newsvalues[0]}:\n" # ID e Titulo
                    #f"{newsvalues[1]}\n" #Texto
                    f" ❤ {newsvalues[4]} | Publicado por @{newsvalues[2]} | {newsvalues[3]}\n"
                    f"{horbar(horbar)}"
                )
        if (islistreversed == True):
            for i in range (len(newsdict), -1, -1):
                if i == 0: break
                newsvalues = newsdict[str(i)]
                print(
                    f"ID[{i}] {newsvalues[0]}:\n" # ID e Titulo
                    #f"{newsvalues[1]}\n" #Texto
                    f" ❤ {newsvalues[4]} | Publicado por @{newsvalues[2]} | {newsvalues[3]}\n"
                    f"{horbar(horbar)}"
                )
        print(
            "Digite o [ID] para ver a notícia.\n"
            "[*]Para reverter ordem da lista\n"
            "[0]Para voltar."
        )
        userchoice = input(">> ")
        if (userchoice == "0"):
            break
        if (userchoice == "*"):
            if (islistreversed == False):
                islistreversed = True
            else:
                islistreversed = False
            continue
        if (userchoice in newsdict):
            viewnews(userinput, userchoice)
        else:
            print("Opção inválida ou ID de notícia não existe.")
            input("Enter para continuar.")
            continue

   
def recentnews ():
    newsvalues = newsdict[str(len(newsdict))]
    print(
        "Notícia mais recente:\n"
        f"ID[{len(newsdict)}] {newsvalues[0]}:\n" #Titulo
        f"{newsvalues[1]}\n" #Texto
        f" ❤ {newsvalues[4]} | Publicado por @{newsvalues[2]} | {newsvalues[3]}\n"
        f"{horbar(horbar)}"
    )


def postnew (userinput):
    verspace()
    title = str(input("Insira o título:\n>> "))
    body = str(input("Insira o texto:\n>> "))
    while True:
        verspace()
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
            likes = 0
            newsid = str(len(newsdict) + 1)
            newsvalues = [title, body, (userinput),(dateandtime()), likes, []]
            newsdict[newsid] = newsvalues
            #print(newsdict)
            break


def logged (userinput="guest"):
    while True:
        verspace()
        recentnews()
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
        
        #Sair
        if (userloggedchoice == "0"):
            verspace()
            break
        
        if userlist[userinput][2] == "GUEST":
            if (userloggedchoice == "2"):
                listnews(userinput)
        
        #Opções de usuário
        if userlist[userinput][2] == "USER":
            if (userloggedchoice == "2"):
                listnews(userinput)

        #Opções de administrador
        if userlist[userinput][2] == "ADM":
            if (userloggedchoice == "2"):
                listnews(userinput)
            if (userloggedchoice == "4"):
                postnew(userinput)


def main ():
    while True:
        recentnews()
        print("Bem vindo, selecione sua opção:")
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
                        print('A senha digitada está incorreta. Tente novamente.')
                        continue
                    
                else:
                    print("O login não existe ou o usuário está incorreto. Tente novamente.")
                    continue
        #Login como convidado
        if (menuchoice == "3"):
            logged()
            

main()