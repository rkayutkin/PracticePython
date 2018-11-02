import random

def game():
    answer = random.randint(1, 10)
    print (answer)
    while True:
        try:
            userguess = int(input("Guess a number between 1 and 9:\n"))
        except ValueError:
            print ("Please enter a number!!!\n")
            continue
        if userguess < answer:
            print ("Aim Higher!!!\n")
            continue
        elif userguess > answer:
            print ("Aim lower!!!\n")
            continue
        elif answer == userguess:
            print ("You have guessed the correct number!!\n")
            repeat = input("Would you like to play again?\n")
            break
    return repeatgame(repeat)

def repeatgame(repeat):
    while True:
        if repeat in ["no", "n"]:
            print ("Thanks for playing!!!\n")
            break
        elif repeat in ["yes", "y"]:
            return game()
        elif repeat in ["exit", "e"]:
            print (exit())
            break
        else:
            print ("Please Choose a valid option!!\n ")
            repeat = input("Would you like to play again?\n ")
game()
