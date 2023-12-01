from funs.clifun import horbar, verspace
from funs.tempdata import userlist, newsdict, comlist, data_import, data_export
from funs.sortlikesfun import listByLikes

def bubblesort (array, args):
    newsList = []
    for item_list in range(0, len(array)+1):
        try:
            
            newsList.insert(item_list, (array[str(item_list + 1)]))
            # print("ok")
        except KeyError:
            continue
    
    while True:
        swapCount = False
        for x in range (0, len(newsList)):
            try:
                if newsList[x][args] > newsList[x+1][args]:
                    # print('ok')
                    swap_aux = newsList[x+1]
                    newsList.pop(x+1)
                    newsList.insert(x, swap_aux)
                    swapCount = True
            except IndexError:
                swapCount = False
                continue
        if swapCount == False:
            break
    # listByLikes(newsList)
    listByLikes(newsList)
    return newsList


print(bubblesort(newsdict, 4))
