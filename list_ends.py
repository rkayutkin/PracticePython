a = [5, 10, 15, 20, 25]
b=[]

def listend(a, b):
    b.append(a[0])
    b.append(a[len(a)-1])
    print (b)
    
listend(a, b)
