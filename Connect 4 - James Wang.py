"""Author: James WAng
   Date: Mar 5, 2019
   Description: A Connect 4 game, that includes a hall of fame for those who 
   beat it, a bot with an attitude, and supports boards from 5x6 to 7x8, and
   prints an appropriate output based on the result of the game."""


import random

def printBoard(board,listNumCol):
    """prints the board"""
    rowNum, numCol = len(board), len(listNumCol)
    print("  " + " ---" * numCol)
    for row in range(rowNum-1,-1,-1):
        print(rowNum , "|", " | ".join(board[row]),"|\n  " + " ---" * numCol)        
        rowNum -= 1
    print("    " + "   ".join(listNumCol))
  
def winner(board):
    """checks to see if either the computer or the user has one, or if the board
       is full and no one has won. Returns the result of the check."""
    for row in board:                   #horizontal victory
        for col in range(len(row) - 3):
            if row[col] == row[col+1] == row[col+2] == row[col+3] != " ":
                return row[col]
            
    for col in range(len(board[0])):    #vertical victory
        for row in range(len(board)-3):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] != " ":
                return board[row][col]
    
    for row in range(len(board) - 3):   #diagonal from bottom left to top right
        for col in range(row - 3):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] != " ":
                return board[row][col]
            
    for row in range(3,len(board)):   #diagonal from top left to bottom right
        for col in range(len(board[0])-3):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] != " ":
                    return board[row][col]

    for space in board[-1]:
        if space == " ":
            return False
        
    return "No winner"
            
def gameMain(first):
    """The game's main function. Calls the winner, userTurn, and computerTurn
       functions in order and with parameters based on input from the user. 
       Returns the result of the game."""
    validCols, validRows = False, False
    while not validCols:   #input validation for the desired number of columns
        numCol = input("Numer of columns(6-8): ")
        if numCol.isdigit() and int(numCol) in range(6,9):
            numCol = int(numCol)
            validCols = True
        else:
            print("Sorry, thats not a vaid choice, Try again")
            
    while not validRows:    #input validation for the desired number of rows
        numRow = input("Numer of rows(5-7): ")
        if numRow.isdigit() and int(numRow) in range(5,8):
            numRow = int(numRow)
            validRows = True
        else:
            print("Sorry, thats not a vaid choice, Try again")
            
    board, listColNum = [], []
    for rows in range(numRow):
        board += [[" "] * numCol]
    for index in range(1,numCol+1):
        listColNum += str(index)
    printBoard(board,listColNum)
    turn = 1
    
    while not winner(board):    #the game runs until winner() has a boolean value True
        if first == "y":         #if the user goes first
            if turn%2 != 0:
                board = userTurn(board)
            else:
                board = computerTurn(board)
        else:                       #if the computer goes first
            if turn%2 == 0:
                board = userTurn(board)
            else:
                board = computerTurn(board)
        printBoard(board,listColNum)
        turn += 1

    return winner(board)            #returns whoever wins

def userTurn(board):
    """Gets the board as a parameter, and returns the changed board after the 
       player has made their move."""
    validMove = False           
    while not validMove:         #input validation for the player's move
        move = input("Column: ")
        if move.isdigit() == True and int(move) in range(1, len(board[0]) +1):
                move = int(move) - 1
                if board[-1][move] != " ":
                    print("Sorry, theres no more space in that column. Try again")
                else:
                    validMove = True
        else:
            print("Thats not a valid choice. Try again")
            
    for row in board:           #adds the player's piece to desired(valid) column
        if row[move] == " ":
            row[move] = "X"   
            return board

def computerTurn(board):
    """Takes the board as a parameter and randomly chooses rows until it finds
       one with at least 1 empty space. Returns the changed board with the
       computer's move."""
    validMove = False
    while not validMove:        #validation
        col = random.randrange(len(board[1]))
        if board[-1][col] == " ":
            validMove = True
    for row in board:
        if row[col] == " ":
            row[col] = "O"   
            return board

def main():
    """The main function. Prints the previous winners from "Hall Of Fame.txt". 
       If it doesn't exist, has appropriate output. Gets input from user for 
       whether they want to go first and the number of columns and rows."""
       
    valid = False
    try:                #checks to see if "Hall Of Fame.txt" exists
        winNum = 0
        winRecord = open("Hall Of Fame.txt","r")
        print("Champions:")
        for name in winRecord:
            winNum += 1
            print(str(winNum) + ". " + name, end="")
        winRecord.close()
    except FileNotFoundError:   #if the file is not found
        print("No Human Has Ever Beat me ... MWAH-HA-HA-HA!")
        
    while not valid:        #input validation for if the player wants to go first or not
        first = input("\nWould you like to go first? (Y/N)\n")
        if first in "YyNn" and len(first) == 1:
            valid = True
        else:
            print("I don't understand. Please try again")
    whoWin = gameMain(first.lower())        #starts the game with player's input
    #when the game has ended, resulting in a tie, win, or lose for the player
    if whoWin == "X":           #if the player wins
        winnerName = input("You Win!\nWhat is your name, champion?\n")
        winRecord = open("Hall Of Fame.txt","a").write(winnerName + "\n")
        winRecord.close()
        print("I will remember you... UNITL WE MEET AGAIN!")
    elif whoWin == "O":         #if the computer wins
        print("You lose! You will never beat me!")
    else:                       #if its a stalemate
        print("Its a tie! You're not bad...")    

main()