import random

def duplicate():
    print ("This is Task 1")
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print (a)
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print (b)
    c = []
    for i in a:
        if i in b:
            c.append(i)
    print (list(set(c)))

def duplicaterandom():
    print ("This is Task 2")
    d = random.sample(range(1, 20), 5)
    print (d)
    e = random.sample(range(1, 20), 8)
    print (e)
    f = []
    for i in d:
        if i in e:
            f.append(i)
            print (list(set(f)))
            break
        elif f == []:
            print("No Duplcates were found")
            break
        else:
            print (f)
            break

duplicate()
duplicaterandom()
