from itertools import chain
def solution(redirects):
    #Calculate destinations by getting values that only appear on right hand side
    destinations = list(set(chain(*redirects)))
    for x in range(len(redirects)):
        if (redirects[x][0] in destinations):
            destinations.remove(redirects[x][0])
    destinations.sort()
    #For each starting point, calculate destination and add to list. 
    
    result = [[destinations[x]] for x in range(len(destinations))]
    listleft, listright = zip(*redirects)
    for y in range(len(redirects)):
        destination = finddestination(redirects[y][0], redirects, listleft)
        destindex = destinations.index(destination)
        result[destindex].append(redirects[y][0])
    
    for x in range(len(result)):
        result[x].sort()
    return result
    
#Recursive method for finding destination. Searches left hand side for input, then returns right hand side value if right hand side value not found on left hand side
def finddestination(start, redirects, listleft):
    index = listleft.index(start)
    result = redirects[index][1]
    if (result in listleft):
        result = finddestination(redirects[index][1], redirects, listleft)
    return result
