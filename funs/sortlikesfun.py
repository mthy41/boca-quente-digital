from funs.clifun import horbar, verspace
from funs.tempdata import newsdict
from funs.viewnewsfun import viewnews

def listByLikes (userinput, bubbleSortedList):
    verspace()
    
    # Ignorar todas as noticias apagadas da lista
    while True:
        removed = False
        for newsRemove in range (0, len(bubbleSortedList)):
            if bubbleSortedList[newsRemove][6] == "DELETED=TRUE":
                bubbleSortedList.pop(newsRemove)
                removed = True
                break
        if removed == False: break
            
    isListreversed = False
    isAuthorFiltered = False
    # print(len(bubbleSortedList))
    while True:
        if isListreversed == False:
            for news in range(0, len(bubbleSortedList)):
                # if bubbleSortedList[news][6] == "DELETED=TRUE":
                #     continue
                print(
                    f"ID[{news + 1}] {bubbleSortedList[news][0]}:\n"
                    f" ❤ {bubbleSortedList[news][4]} | Publicado por @{bubbleSortedList[news][2]} | {bubbleSortedList[news][3]}\n"
                    f"{horbar(horbar)}"
                    # f"{bubbleSortedList[news][6]}"
                )
        if isListreversed == True:
            for news in reversed(range(0, len(bubbleSortedList))):
                # if news == 0: break
                print(
                    f"ID[{news + 1}] {bubbleSortedList[news][0]}:\n"
                    f" ❤ {bubbleSortedList[news][4]} | Publicado por @{bubbleSortedList[news][2]} | {bubbleSortedList[news][3]}\n"
                    f"{horbar(horbar)}"
                )
        # break    
        print(
            "Digite o [ID] para ver a notícia ou:\n"
            "[*]Para reverter ordem da lista\n"
            "[t]Ordenar por tempo de publicação.\n"
            "[0]Para voltar."
        )
        userChoice = input(">> ")
        
        
        if userChoice == "0":
            return "C"

        if userChoice == "t" or userChoice == "T":
            break
        
        if userChoice == "*":
            if isListreversed == False:
                isListreversed = True
                continue
            if isListreversed == True:
                isListreversed = False
                continue

        if (userChoice in newsdict):
            newsvalues = newsdict[userChoice]
            if (newsvalues[6] == "DELETED=FALSE"):
                viewnews(userinput, userChoice)
            else:
                print("Opção inválida ou ID de notícia não existe.")
                input("Enter para continuar.")
                continue

        # else:
        if not (userChoice in newsdict):
            print("Opção inválida ou ID de notícia não existe.")
            input("Enter para continuar.")
            continue

        
        








