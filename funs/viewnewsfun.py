from funs.tempdata import userlist, newsdict, comlist
from funs.clifun import verspace, horbar
from funs.addcomfun import addcom
from funs.viewcomfun import viewcom

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
            if uservalues[2] == "GUEST":
                print("Você precisa fazer login para poder curtir publicações.")
                input("Pressione enter para voltar.")
                continue
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
