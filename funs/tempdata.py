#Estrutura de dados:
#"user":["senha", "nome completo", "cargo", [ids de noticias curtidas], [ids de noticias publicadas]]
#o [ids de noticias publicadas] apenas para usuarios do cargo ADM
import json


userlist = {}

newsdict = {}

comlist = {}

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
    