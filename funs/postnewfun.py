import datetime

from funs.tempdata import userlist, newsdict, comlist
from funs.clifun import horbar, verspace


def dateandtime ():
    now = datetime.datetime.now()
    format = "%Y-%m-%d %H:%M:%S"
    currentTime = now.strftime(format)
    return(currentTime)

def postnew (userinput):
    verspace()
    title = str(input("Insira o título:\n>> "))
    body = str(input("Insira o texto:\n>> "))
    while True:
        verspace()
        print(
            f"Título: {title}\n"
            f"Texto: {body}\n"
            "[1]Adicionar ou editar título.\n"
            "[2]Adicionar ou editar texto.\n"
            "[3]Publicar.\n"
            "[0]Sair.\n"
        )
        #Voltar
        userchoicepostnew = str(input())
        if (userchoicepostnew == "0"):
            while True:
                userchoicesure = str(input("Deseja sair sem salvar? [0] para sim ou [1] para cancelar.\n>> "))
                if (userchoicesure == "0"):
                    break
                elif (userchoicesure == "1"):
                    break
                else:
                    print("Opção inválida.")
                    continue
            if (userchoicesure == "1"):
                continue
            break

        #Add titulo
        if (userchoicepostnew == "1"):
            title = str(input("Insira o novo título:\n>> "))

        #Add texto
        if (userchoicepostnew == "2"):
            body = str(input("Insira o novo texto:\n>> "))

        #Publicar
        if (userchoicepostnew == "3"):
            likes = 0
            newsid = str(len(newsdict) + 1)
            newsvalues = [title, body, (userinput),(dateandtime()), likes, [], "DELETED=FALSE"]
            newsdict[newsid] = newsvalues
            #print(newsdict)
            break
