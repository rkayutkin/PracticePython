a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b =[]
c= []

# This is Taks 1
print ("This is Taks 1: ")
for element in a:
    if element < 5:
        print (element)
print()
print ("This is Taks 2: ")
for element in a:
    if element < 5: b.append(element)
print (b)
print()
print ("This is Taks 3: ")
print([i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if i < 5])
print()
print ("This is Taks 4: ")
# This is Task 4
def list(num):
    for element in a:
        if element < num: c.append(element)
    print(c)

list(num= int(input("Please enter a number: ")))
