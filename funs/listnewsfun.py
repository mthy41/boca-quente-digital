from funs.tempdata import userlist, newsdict, comlist
from funs.clifun import verspace, horbar
from funs.viewnewsfun import viewnews
from funs.sortalg import bubblesort as bubblesort

def listnews (userinput):
    islistreversed = False #Ordem padrão (das mais velhas as mais novas)
    while True:
        verspace()
        if (islistreversed == False):
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
        if (islistreversed == True):
            for i in range (len(newsdict), -1, -1):
                if i == 0: break
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
            "Digite o [ID] para ver a notícia.\n"
            "[*]Para reverter ordem da lista\n"
            "[c]Ordenar por curtidas.\n"
            "[0]Para voltar."
        )
        userchoice = input(">> ")
        if (userchoice == "c" or userchoice == "C"):
            bubblesort(newsdict, 4)
        if (userchoice == "0"):
            break
        if (userchoice == "*"):
            if (islistreversed == False):
                islistreversed = True
            else:
                islistreversed = False
            continue
        if (userchoice in newsdict):
            newsvalues = newsdict[userchoice]
            if (newsvalues[6] == "DELETED=FALSE"):
                viewnews(userinput, userchoice)
            else:
                print("Opção inválida ou ID de notícia não existe.")
                input("Enter para continuar.")
                continue

        else:
            print("Opção inválida ou ID de notícia não existe.")
            input("Enter para continuar.")
            continue