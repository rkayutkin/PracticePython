import os

def players():
    while True:
        os.system('clear')
        print ("Welcome to the simple game of Rock, Paper, Scissors!!!\n\n ")
        Player1 = input("Player 1, please choose one option: \n-Rock \n-Paper \n-Scissors\n\n ")
        Player1 = Player1.lower()
        if Player1 in ["rock", "paper", "scissors"]:
            break
        elif Player1 in ["exit", "quit"]:
            print ("Thaks for playing!!!\n ")
            print (exit())
            break
        else:
            print ("Player 1 didn't choose a valid option.\n ")
            continue
    while True:
        os.system('clear')
        Player2 = input("Player 2, please choose one option: \n-Rock \n-Paper \n-Scissors\n\n ")
        Player2 = Player2.lower()
        if Player2 in ["rock", "paper", "scissors"]:
            break
        elif Player2 in ["exit", "quit"]:
            print ("Thaks for playing!!!\n ")
            print (exit())
            break
        else:
            print ("Player 2 didn't choose a valid option.\n ")
            continue
    return logic(Player1, Player2)

def logic(Player1, Player2):
    os.system('clear')
    if Player1 == "paper" and Player2 == "rock":
        print ("Congragulations Player 1!!!")
        repeat = input("Would you like to play again?:\n ")
    elif Player2 == "paper" and Player1 == "rock":
        print ("Congragulations Player 2!!!")
        repeat = input("Would you like to play again?:\n ")
    elif Player1 == "rock" and Player2 == "scissors":
        print ("Congragulations Player 1!!!")
        repeat = input("Would you like to play again?:\n ")
    elif Player2 == "rock" and Player1 == "scissors":
        print ("Congragulations Player 2!!!")
        repeat = input("Would you like to play again?:\n ")
    elif Player1 == "scissors" and Player2 == "paper":
        print ("Congragulations Player 1!!!")
        repeat = input("Would you like to play again?:\n ")
    elif Player2 == "scissors" and Player1 == "paper":
        print ("Congragulations Player 2!!!")
        repeat = input("Would you like to play again?:\n ")
    elif Player1 == Player2:
        print ("Its a DRAW!!!")
        repeat = input("Would you like to play again?:\n ")
    elif Player1 == exit:
        print ("Thaks for playing!!!\n ")
        print (exit())
    elif Player2 == exit:
        print ("Thaks for playing!!!\n ")
        print (exit())
    while True:
        os.system('clear')
        if repeat == "no":
            print ("Thaks for playing!!!\n ")
            os.system('clear')
            break
        if repeat == "yes":
            return players()
        if repeat in ["exit", "quit"]:
            print ("Thaks for playing!!!\n ")
            os.system('clear')
            print (exit())
        else:
            print ("Please Choose a valid option!!\n ")
            os.system('clear')
            repeat = input("Would you like to play again?:\n ")

players()

# def player2():
#     while True:
#         Player2 = input("Player 2, please choose one option: \n-Rock \n-Paper \n-Scissors\n ")
#         Player2 = Player2.lower()
#         if Player2 in ["rock", "paper", "scissors"]:
#             print ("Yes")
#             break
#         else:
#             print ("Player 2 didn't choose a valid option")
#             continue
#     return logic(Player2)
