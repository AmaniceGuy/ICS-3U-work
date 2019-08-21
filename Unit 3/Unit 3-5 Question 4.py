"""James Wang
   Jan 14, 2019
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
    
def main():
    word = input("word: ")
    newWord = word_jumble(word)
    print(scramWood)

main()