def setremoval():
    a = [1,2,4,1,1,6,4,5,3,2,7,8,9,9]
    new = []
    for i in a:
        new.append(i)


    print (list(set(new)))

def loopremoval():
    a = [1,2,4,1,1,6,4,5,3,2,7,8,6,9,9,8]
    new = []
    for i in a:
        if i not in new:
            new.append(i)

    print (new)

setremoval()
loopremoval()
