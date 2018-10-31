number = int(input("Please enter a number: "))
a = range(1, (number+1))
dl = []

for i in a:
    if number % i == 0:
        dl.append(i)

print ()
print (dl)
