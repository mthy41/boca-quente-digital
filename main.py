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


def searchnews (userinput):
    while True:
        verspace()
        for i in range (1, (len(newsdict) + 1)):
            newsvalues = newsdict[str(i)]
            print(
                f"ID[{i}] {newsvalues[0]}:\n" # ID e Titulo
                #f"{newsvalues[1]}\n" #Texto
                f" ❤ {newsvalues[4]} | Publicado por @{newsvalues[2]} | {newsvalues[3]}\n"
                f"{horbar(horbar)}"
            )
        print(
        "Selecione uma opção.\n"
        "[1]Procurar por ID.\n"
        "[2]Procurar por título.\n"
        "[0]Sair."
    )
        searchnewschoice = input("")
        
        if (searchnewschoice == "0"):
            break
        if (searchnewschoice == "1"):
            idsearch = input("ID: ")
            if (idsearch in newsdict):
                viewnews(userinput, idsearch)
            else:
                print("ID inválido ou notícia não existe.")
                input("Pressione enter para continuar")
            continue
        if (searchnewschoice == "2"):
            titlesearch = input("Título: ")
            for i in newsdict:
                values = newsdict[i]
                if (titlesearch == values[0]):
                    viewnews(userinput, i)
                    continue
            input("Notícia não encontrada.\nPressione enter para continuar.")


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

        if userlist[userinput][1] == "GUEST":
            if (userloggedchoice == "2"):
                searchnews(userinput)
        
        if userlist[userinput][1] == "USER":
            if (userloggedchoice == "2"):
                searchnews(userinput)
                
        if userlist[userinput][2] == "ADM":
            if (userloggedchoice == "1"):
                searchnews(userinput)
        
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