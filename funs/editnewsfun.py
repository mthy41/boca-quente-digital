from funs.tempdata import *
from funs.clifun import *
#from funs.viewnewsfun import viewnews
from colorama import Fore, Style

def newsedit(userinput, idsearch="*"):
    while True:
        verspace()
        if (idsearch == "*"):
            idsearch = input("[0]Voltar.\nID: ")
        if (idsearch == "0"):
            break
        if (idsearch in newsdict):
            newsvalues = newsdict[idsearch]
        if userinput != newsvalues[2]:
            print("Você não é o autor desta publicação.")
            input("Pressione enter para continuar.")
            break
        if (newsvalues[6] == "DELETED=FALSE"):
            while True:
                verspace()
                print(
                    f"{Style.BRIGHT}Título:{Style.RESET_ALL} {newsvalues[0]}\n"
                    f"{Style.BRIGHT}Texto:{Style.RESET_ALL} {newsvalues[1]}"
                )
                print(
                    f"[1]Adicionar ou editar título.\n"
                    f"[2]Adicionar ou editar novo texto.\n"
                    f"[0]Sair."
                )
                editnewschoice = input(">> ")
                if (editnewschoice == "0"):
                    break
                if (editnewschoice == "1"):
                    newsvalues[0] = str(input("Insira novo título.\n>> "))
                    #newsdict[idsearch] = newsvalues
                    continue
                if (editnewschoice == "2"):
                    newsvalues[1] = str(input("Digite novo texto.\n>> "))
        else:
            print("Opção inválida ou ID de notícia não existe.")
            input("Enter para continuar.")
            break
        #else:
        #    print("ID inválido ou notícia não existe.")
        #    input("Pressione enter para continuar")
        break