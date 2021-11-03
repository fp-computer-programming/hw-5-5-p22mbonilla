# Author MB 11/02/2021

word = input("enter first word: ")
word2 = input("enter second word: ")
word3 = input("enter third word: ")

a = str.capitalize(word)
b = str.capitalize(word2)
c = str.capitalize(word3)

if a > b and a > c:
    if b > c:
        print(word, word2, word3)
elif a > b and a < c:
    if b < c:
        print(word2, word3, word)
elif a < b and a < c:
    if b > c:
        print(word2, word, word3)
elif a < b and a < c:
    if b > c:
        print(word2, word, word3)
elif a < b and a < c:
    if b < c:
        print(word3, word2, word)
elif a > b and a < c:
    if b < c:
        print(word3, word, word2)