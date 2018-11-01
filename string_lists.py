word = input("Please enter a word: ")
e = word[::-1]

if word.lower() == e:
    print ("This word is palindrome")
elif word.lower() != e:
    print ("This word is not a palindrome")
else:
    print ("Pick another word")
