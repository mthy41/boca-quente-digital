from funs.tempdata import userlist, newsdict, comlist
from funs.clifun import horbar, verspace
from funs.addcomfun import addcom
from colorama import *

def viewcom (userinput, uservalues, userchoice):
    while True:
        verspace()
        newsvalues = newsdict[userchoice]
        for i in (newsvalues[5]):
            comvalues = comlist[i]
            print(f"{Style.BRIGHT}@{comvalues[1]}{Style.RESET_ALL}: {comvalues[2]}")
            print(horbar(horbar))
        
        print(
            "[0]Sair."
        )
        if uservalues[2] == "USER" or uservalues[2] == "ADM":
            print(
            "[1]Adicionar comentário.\n"
            )
            
        userviewcomchoice = input("")
        
        #Sair
        if (userviewcomchoice == "0"):
            break
        
        #Adicionar comentário
        if (uservalues[2] != "GUEST"):
            if (userviewcomchoice == "1"):
                addcom(userinput, uservalues, userchoice, newsvalues)
                #break