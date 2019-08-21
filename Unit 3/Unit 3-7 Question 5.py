"""James Wang
   Jan 22, 2019
"""
import random

def word_jumble(word):
    new = ""
    count = len(word)
    for i in range(count):
        letter = random.randint(0,count-1)
        new += word[letter]
        word = word[:letter] + word[letter+1:]
        count -= 1
    return new

def game_main():
    wordList = ["hi", "hello", "salut", "hey", "good day"]
    for turn in range(5):
        x = random.randrange(len(wordList))
        print(word_jumble(wordList[x]))
        guess = input("Guess what it is? ")
        while guess != wordList[x]:
            guess = input("Guess what it is? ")
        del wordList [x]
        print("Correct")

game_main()