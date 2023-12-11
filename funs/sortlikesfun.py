from funs.clifun import horbar, verspace
from funs.tempdata import newsdict, userlist
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
    authorFilterOpt = "[a]Filtrar por autor."
    authorNews = True
    # print(len(bubbleSortedList))
    while True:
        verspace()
        if isListreversed == False:
            for news in range(0, len(bubbleSortedList)):
                if isAuthorFiltered == True:
                    newsvalues = bubbleSortedList[news]
                    if not newsvalues[2] == authorChoice:
                        continue
                print(
                    f"ID[{news + 1}] {bubbleSortedList[news][0]}:\n"
                    f" ❤ {bubbleSortedList[news][4]} | Publicado por @{bubbleSortedList[news][2]} | {bubbleSortedList[news][3]}\n"
                    f"{horbar(horbar)}"
                    # f"{bubbleSortedList[news][6]}"
                )
        if isListreversed == True:
            for news in range(0, len(bubbleSortedList)):
                if isAuthorFiltered == True:
                    newsvalues = bubbleSortedList[news]
                    if not newsvalues[2] == authorChoice:
                        continue
            for news in reversed(range(0, len(bubbleSortedList))):
                # if news == 0: break
                print(
                    f"ID[{news + 1}] {bubbleSortedList[news][0]}:\n"
                    f" ❤ {bubbleSortedList[news][4]} | Publicado por @{bubbleSortedList[news][2]} | {bubbleSortedList[news][3]}\n"
                    f"{horbar(horbar)}"
                )
        # break    
        print(
            f"Digite o [ID] para ver a notícia ou:\n"
            f"[t]Ordenar por tempo de publicação.\n"
            f"{authorFilterOpt}\n"
            # f"[*]Para reverter ordem da lista\n"
            f"[0]Para voltar."
        )
        userChoice = input(">> ")
        
        
        if userChoice == "0":
            return "C"

        if userChoice == "t" or userChoice == "T":
            break
        
        if userChoice == "a" or userChoice == "A":
            if isAuthorFiltered == False:
                verspace()
                print("Insira o @ do autor:")
                authorChoice = input(">> ")
                if not authorChoice in userlist:
                    verspace()
                    print("Este usuário não existe.")
                    input("Pressione enter para continuar.\n>> ")
                    continue
                if authorChoice in userlist:
                    if not userlist[authorChoice][2] == "ADM":
                        print("O usuário não é um autor(a).")
                        input("Pressione enter para continuar.\n>> ")
                        continue
                    authorFilterOpt = "[a]Remover filtro."
                    isAuthorFiltered = True
                    authorNews = False
                    continue
                    for news in bubbleSortedList:
                        if news[2] == authorChoice and news[6] == "DELETED=FALSE":
                            authorNews = True
                if authorNews == True:
                    authorFilterOpt = "[a]Remover filtro."
                    isAuthorFiltered = True
                    continue
                else:
                    verspace()
                    authorNews = False                
                verspace()
                continue
            if isAuthorFiltered == True:
                authorFilterOpt = "[a]Filtrar por autor."
                isAuthorFiltered = False
                verspace()
                continue
            
        
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

        
        








