def reverse():
    inputuser= input("Please provide a word or sentance:\n")
    result= ' '.join(inputuser.split()[::-1])
    print (result)

def reverse2():
    inputuser= input("Please provide a word or sentance:\n")
    result= inputuser.split()
    result.reverse()
    result= " ".join (result)

    print (result)

reverse()
reverse2()
