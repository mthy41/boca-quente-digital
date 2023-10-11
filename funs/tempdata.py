#Estrutura de dados:
#"user":["senha", "nome completo", "cargo", [ids de noticias curtidas], [ids de noticias publicadas]]
#o [ids de noticias publicadas] apenas para usuarios do cargo ADM
import json
import os

userlist = {}

newsdict = {
    "2":["GRAVE! Prefeito de Cajazeiras cancela natal por falta de verba", "Nesta Quinta-Feira, o prefeito sancionou uma lei municipal que proibe qualquer tipo de comemoração, pública ou privada, relacionada ao natal.", "choquei", "1964.23.12 - 00:00", 666]
        
    }

comlist = {}



def data_export ():
    base_dir = os.path.dirname(os.path.dirname(__file__))

    userlist_path = (os.path.join(base_dir, "data", "userlistdata.json"))
    with open (userlist_path, "w") as ulp:
        json.dump(userlist, ulp, indent=1)

    newsdict_path = (os.path.join(base_dir, "data", "newsdictdata.json"))
    with open (newsdict_path, "w") as ndp:
        json.dump(newsdict, ndp, indent=1)

    comlist_path = (os.path.join(base_dir, "data", "comlistdata.json"))
    with open (comlist_path, "w") as clp:
        json.dump(comlist, clp, indent=1)

def data_import():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    
    userlist_path = (os.path.join(base_dir, "data", "userlistdata.json"))
    with open (userlist_path, "r") as ulp:
        userlistdataload = json.load(ulp)
    userlist.update(userlistdataload)

    newsdict_path = (os.path.join(base_dir, "data", "newsdictdata.json"))
    with open (newsdict_path, "r") as ndp:
        newsdictdataload = json.load(ndp)
    newsdict.update(newsdictdataload)

    comlist_path = (os.path.join(base_dir, "data", "comlistdata.json"))
    with open (comlist_path, "r") as clp:
        comlistdataload = json.load(clp)
    comlist.update(comlistdataload)
    