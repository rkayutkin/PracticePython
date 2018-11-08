def fibonacci():
    while True:
        try:
            num = int(input("How many fibonacci numbers in a sequence would you like to print: \n"))
            if num == 0:
                print ("Enter a higher numner!!!\n")
                continue
        except ValueError:
            print ("Please Enter a number!!!\n")
            continue
        a = 1
        b = 1
        list=[1,]

        for i in range(num):
            a, b = b, a + b
            list.append(a)
        print (list)

fibonacci()
