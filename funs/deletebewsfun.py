from funs.tempdata import *
from funs.clifun import *
from colorama import Fore, Style

def newsdelete (userinput):
    while True:
        verspace()
        print(
            f"Digite o ID da notícia a ser apagada.\n"
            f"Ou [0] para voltar.\n"
            f"NOTA: você só pode excluir notícias que você publicou."

        )
        newsdeletechoice = input(">> ")
        if (newsdeletechoice == "0"):
            break
        if (not newsdeletechoice in newsdict):
            print(Fore.YELLOW + "Não existe nenhuma notícia vinculada à esse ID.")
            input(Style.BRIGHT + "Pressione enter para voltar.")
            continue
        newsvalues = newsdict[newsdeletechoice]
        if (newsvalues[6] == "DELETED=TRUE"):
            print(Fore.YELLOW + "Não existe nenhuma notícia vinculada à esse ID.")
            input(Style.BRIGHT + "Pressione enter para voltar.")
            continue
        if (newsvalues[2] != userinput):
            print(Fore.YELLOW + "Negado: Você não é o autor desta publicação.")
            input(Style.BRIGHT + "Pressione enter para voltar.")
            continue
        
        #Confirmação
        print(f"Tem certeza que deseja apagar a notícia de ID: {newsdeletechoice}?")
        confirm =  input(
            f"[1] Sim.\n"
            f"[0]Não.\n>> "
        )
        if (confirm == "0"):
            continue
        if (confirm == "1"):
            newsvalues[0] = "[PUBLICAÇÃO EXCLUÍDA]"
            newsvalues[1] = ""
            newsvalues[5] = []
            newsvalues[6] = "DELETED=TRUE"
            newsdict[newsdeletechoice] = newsvalues
            print(newsvalues)
        else:
            print("Opção inválida")
            input("Pressione enter para continuar.")
