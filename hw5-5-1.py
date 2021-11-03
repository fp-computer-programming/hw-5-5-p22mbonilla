# Author MB 11/02/2021

word = input("enter a word: ")
length = len(word)
length //= 2
print(word[:length])
print(word[length:])