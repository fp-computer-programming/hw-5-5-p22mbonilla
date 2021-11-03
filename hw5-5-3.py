# Author MB 11/02/2021

word = input("enter a string: ")
word2 = word[::-1]
if word2 == word:
    print(word2)
    print(word)
else:
    print("Not a palindrome")