from funs.tempdata import userlist, newsdict, comlist
from funs.clifun import verspace, horbar
from funs.viewnewsfun import viewnews

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