#loss prevention and finishing 
for row in range(3):
    if (board[row][0] == board[row][1]) and board[row][2]:
        board[row][2] = 'O'
    elif (board[row][1] == board[row][2]) and board[row][0]:
        board[row][0] = 'O'
    elif (board[row][0] == board[row][2]) and board[row][1]:
        board[row][1] = 'O'    
    
    
for col in range(3):
    if (board[0][col] == board[1][col]) and board[2][col]:
        board[2][col] = 'O'
    elif (board[1][col] == board[2][col]) and board[0][col]:
        board[0][col] = 'O'
    elif (board[0][col] == board[2][col]) and board[1][col]:
        board[1][col] = 'O'
    
if 