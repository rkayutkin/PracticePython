num= int(input("Pleae enter the first number: "))
check= int(input("Pleae enter the second number: "))

if num % 4==0:
    print ("The first number you entered is even and a multiple of 4")
elif num % 2==0:
    print ("The first number you entered is Even")
elif num % 2!=0:
    print ("The first number you entered is Odd")

if check / num==1:
    print ("The first and second numbers you entered can be evenly divided")
if check / num!=1:
    print ("The first and second numbers you entered can't be evenly divided")
