from tempdata import userlist, newsdict, comlist
from clifun import horbar, verspace

def addcom (userinput, userchoice, uservalues, newsvalues):
    verspace()
    com = str(input(
        "Insira seu comentário:\n>> "
    ))
    print(horbar(horbar))
    print(com)
    print(horbar(horbar))
    print(
        "Publicar comentário?\n"
        "[1]Sim.\n"
        "[0]Não."
    )
    comconfirm = input(">> ")
    if (comconfirm == "1"):
        comvalues = [userchoice, userinput, com]
        comlist[str(len(comlist)+1)] = comvalues
        newsvalues[5].append(str(len(comlist)))
    else:
        print("Operação cancelada.")