from funs.tempdata import userlist, newsdict, comlist
from funs.clifun import horbar, verspace
from colorama import *
#Incializar o colorama
init(autoreset=True)

def recentnews ():
    newsvalues = newsdict[str(len(newsdict))]
    print(
        f"{Style.BRIGHT}Notícia mais recente:{Style.RESET_ALL}\n"
        f"ID[{len(newsdict)}] {Style.BRIGHT}{newsvalues[0]}{Style.RESET_ALL}:\n" #Titulo
        f"{newsvalues[1]}\n" #Texto
        f" ❤ {newsvalues[4]} | Publicado por {Style.BRIGHT}@{newsvalues[2]}{Style.RESET_ALL} | {newsvalues[3]}\n"
        f"{horbar(horbar)}"
    )