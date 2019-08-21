import random

def guessing(rangeLow, rangeHigh):
    guessValue = int(rangeLow  + (rangeHigh-rangeLow)/2))
    print("My guess is:", guessValue, end= "\n")
    return guessValue

def main():
    rangeLow = 0
    rangeHigh = 100
    while True == True:
        guess = guessing (rangeLow,rangeHigh)
        print("\nAm I?\n  1. Too low.\n  2. Correct!\n  3. Too high.\n")
        rngUpDown = int(input("\nWhich one: "))
        while True == True:
            if rngUpDown == 1:
                rangeLow = guess
            elif rngUpDown == 3:
                rangeHigh = guess
            elif rngUpDown == 2:
                for x in range (1,100):
                    print("DAB ON THE HATERS")
            else:
                rngUpDown = int(input("nI didn't understand your last answer sorry. Which one: "))
                continue
            break
main()
            