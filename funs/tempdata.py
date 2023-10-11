#Estrutura de dados:
#"user":["senha", "nome completo", "cargo", [ids de noticias curtidas], [ids de noticias publicadas]]
#o [ids de noticias publicadas] apenas para usuarios do cargo ADM
import json


userlist = {
    "guest": ["guest", "convidado", "GUEST",[]],
    "cat": ["123", "Miguel Ohara", "ADM", [],[]],
    "rat":["123", "Kimberlie Schwatson", "USER",[]],
    "dog":["123", "Miles Morales", "USER", []],
    "bird":["123", "Ivan Neves", "USER",[]]
}

newsdict = {
    "1": ["title", "body", "author", "date", 3, []],
    "2": ["title2", "body2", "author2", "date2", 5, ["1", "2"]],
    "3": ["title3", "body3", "author3", "date3", 1, []]
}

comlist = {
    "id do comentario":["id da noticia comentada", "user que comentou", "comentário"],
    "1":["2", "comAuthor", "comText"],
    "2":["2", "dog", "que bosta de noticia"]
}   

def data_export ():
    userlist_path = "projetoP1/data/userlistdata.json"
    with open (userlist_path, "w") as ulp:
        json.dump(userlist, ulp, indent=1)

    newsdict_path = "projetoP1/data/newsdictdata.json"
    with open (newsdict_path, "w") as ndp:
        json.dump(newsdict, ndp, indent=1)

    comlist_path = "projetoP1/data/comlistdata.json"
    with open (comlist_path, "w") as clp:
        json.dump(comlist, clp, indent=1)

def data_import():
    userlist_path = "projetoP1/data/userlistdata.json"
    with open (userlist_path, "r") as ulp:
        userlistdataload = json.load(ulp)
    userlist.update(userlistdataload)

    newsdict_path = "projetoP1/data/newsdictdata.json"
    with open (newsdict_path, "r") as ndp:
        newsdictdataload = json.load(ndp)
    newsdict.update(newsdictdataload)

    comlist_path = "projetoP1/data/comlistdata.json"
    with open (comlist_path, "r") as clp:
        comlistdataload = json.load(clp)
    comlist.update(comlistdataload)
    