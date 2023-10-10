#Estrutura de dados:
#"user":["senha", "nome completo", "cargo", [ids de noticias curtidas], [ids de noticias publicadas]]
#o [ids de noticias publicadas] apenas para usuarios do cargo ADM

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
    #"id do comentario":["id da noticia comentada", "user que comentou", "comentário"]
    "1":["2", "comAuthor", "comText"],
    "2":["2", "dog", "que bosta de noticia"]
}