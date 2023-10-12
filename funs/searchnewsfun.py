from funs.tempdata import userlist, newsdict, comlist
from funs.clifun import horbar, verspace
from funs.viewnewsfun import viewnews

def searchnews (userinput):
    while True:
        verspace()
        for i in range (1, (len(newsdict) + 1)):
            newsvalues = newsdict[str(i)]
            if (newsvalues[6] == "DELETED=TRUE"):
                continue
            else:
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
            if (idsearch == "0"):
                break
            if (idsearch in newsdict):
                newsvalues = newsdict[idsearch]
                if (newsvalues[6] == "DELETED=FALSE"):
                    viewnews(userinput, idsearch)
                else:
                    print("Opção inválida ou ID de notícia não existe.")
                    input("Enter para continuar.")
                    continue
            else:
                print("ID inválido ou notícia não existe.")
                input("Pressione enter para continuar")
            continue
        if (searchnewschoice == "2"):
            titlesearch = input("Título: ")
            if (titlesearch == "0"):
                break
            for i in newsdict:
                values = newsdict[i]
                if (titlesearch == values[0]):
                    if (values[6] == "DELETED=FALSE"):
                        viewnews(userinput, i)
                    else:
                        input("Notícia não encontrada.\nPressione enter para continuar.")
                    continue
            input("Notícia não encontrada.\nPressione enter para continuar.")
