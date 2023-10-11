from funs.tempdata import userlist, newsdict, comlist
from funs.clifun import horbar, verspace

def recentnews ():
    newsvalues = newsdict[str(len(newsdict))]
    print(
        "Notícia mais recente:\n"
        f"ID[{len(newsdict)}] {newsvalues[0]}:\n" #Titulo
        f"{newsvalues[1]}\n" #Texto
        f" ❤ {newsvalues[4]} | Publicado por @{newsvalues[2]} | {newsvalues[3]}\n"
        f"{horbar(horbar)}"
    )