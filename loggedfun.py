from tempdata import userlist, newsdict, comlist
from clifun import verspace, horbar
from recentnewsfun import recentnews
from searchnewsfun import searchnews
from listnewsfun import listnews
from postnewfun import postnew

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
