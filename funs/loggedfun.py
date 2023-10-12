from funs.tempdata import userlist, newsdict, comlist
from funs.clifun import verspace, horbar
from funs.recentnewsfun import recentnews
from funs.searchnewsfun import searchnews
from funs.listnewsfun import listnews
from funs.postnewfun import postnew

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
        
        #Convidade pesquisar
        if userlist[userinput][2] == "GUEST":
            if (userloggedchoice == "1"):
                searchnews(userinput)
        
        #????????????????
        if userlist[userinput][1] == "USER":
            if (userloggedchoice == "2"):
                searchnews(userinput)
                
        #ADM pesquisar
        if userlist[userinput][2] == "ADM":
            if (userloggedchoice == "1"):
                searchnews(userinput)
        
        #Convidade listar
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
