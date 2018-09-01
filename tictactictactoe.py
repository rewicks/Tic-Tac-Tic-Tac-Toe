import random
import Queue
import copy

########globals###########################
board = [['O',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ','X',' ',' ',' ',' ',' ',' '],
         [' ','X',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ','O',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ','O',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' ']]

quadrants = [[0,0,0],[0,0,0],[0,0,0]]

#############displayhelpers#######################

def printboard(board): #9x9 board
    for x in range(0,9):
        rowString = ""
        for y in range(0,9):
            if (board[x][y] != ' '):
                rowString+= (board[x][y])
            elif (x % 3 != 2):
                rowString += ('_')
            else:
                rowString += (' ')
            if (y % 3 == 2 and y != 8):
                rowString += (" || ")
            elif (y != 8):
                rowString += ('|')
        print(rowString)
        if (x %3 == 2 and x != 8):
            print("========================")


#################validations##################     
   
def validMove(lastMove, nextMove, current_board, current_quadrants):
    #print(3*((lastMove[0]%3)+1))
            
    if (current_board[nextMove[0]][nextMove[1]] != ' '):
        return False
    elif (current_quadrants[nextMove[0]/3][nextMove[1]/3] != 0):
        return False
    elif (lastMove == None):
        #print('a')
        return True
    full = True
    for x in range(3*(lastMove[0] % 3),(3*((lastMove[0]%3)+1))):
        for y in range(3 * (lastMove[1] % 3),(3*((lastMove[1]%3) + 1))):
            if(current_board[x][y] == ' '):
                full = False
    if (full):
        #print('b')
        return True
    elif (current_quadrants[lastMove[0]%3][lastMove[1]%3] != 0):
        #print(lastMove, nextMove)
        #printboard(current_board)
        #print('c')
        #print(current_quadrants)
        return True
    elif (nextMove[0] < (3*(lastMove[0] % 3)) or (nextMove[0] >= (3*((lastMove[0]%3)+1)))):
        return False
    elif (nextMove[1] < (3 * (lastMove[1] % 3)) or (nextMove[1] >= (3*((lastMove[1]%3) + 1)))):
        return False
    else:
        #print(lastMove, nextMove)
        #printboard(current_board)
        #print('d')
        return True

def cat(lastMove, current_board, current_quadrants):
    for x in range(0,9):
        for y in range(0,9):
            if (validMove(lastMove, (x,y), current_board, current_quadrants)):
                return False
    return True

def checkWin(board, token, current_quadrants):
    #quadrants = [[False, False, False],[False, False, False],[False,False,False]]
    #for x in range(0, 9):
        #for y in range(0, 9):
            #if (board[x][y] == token):
                
                ##check horizontal
                #if (x%3 == 0 and board[x + 1][y] == token and board[x+2][y] == token):
                    #quadrants[x/3][y/3] = token
                    
                ##check vertical
                #if (y%3 == 0 and board[x][y+1] == token and board[x][y+2] == token):
                    #quadrants[x/3][y/3] = token
                    
                ##check diagonal
                #if (x%3 == 1 and y%3 == 1):
                    #if (board[x-1][y-1] == token and board[x+1][y+1] == token):
                        #quadrants[x/3][y/3] = token
                    #elif (board[x+1][y-1] == token and board[x-1][y+1] == token):
                        #quadrants[x/3][y/3] = token
                        
    #check quadrants board for win
    for x in range(0,3):
        for y in range(0,3):
            if (x == 0 and current_quadrants[x+1][y] == token and current_quadrants[x+2][y] == token):
                return True
            elif (y == 0 and current_quadrants[x][y+1] == token and current_quadrants[x][y+2] == token):
                return True
            elif (y == 1 and x == 1):
                if (current_quadrants[x-1][y-1] == token and current_quadrants[x+1][y+1] == token):
                    return True
                elif (current_quadrants[x+1][y-1] == token and current_quadrants[x-1][y+1] == token):
                    return True
    return False

def updateQuadrants(current_quadrants, current_board):
    #retVal = [[0,0,0],[0,0,0],[0,0,0]]
    for x in range(0, 9):
        for y in range(0, 9):
            if (current_board[x][y] == 'X'):
                #check horizontal
                if (x%3 == 0 and current_board[x + 1][y] == 'X' and current_board[x+2][y] == 'X'):
                    current_quadrants[x/3][y/3] = 'X'
                    #print('a')
                    
                #check vertical
                if (y%3 == 0 and current_board[x][y+1] == 'X' and current_board[x][y+2] == 'X'):
                    current_quadrants[x/3][y/3] = 'X'
                    #print('d')
                    
                #check diagonal
                if (x%3 == 1 and y%3 == 1):
                    if (current_board[x-1][y-1] == 'X' and current_board[x+1][y+1] == 'X'):
                        current_quadrants[x/3][y/3] = 'X'
                        #print('b')
                    elif (current_board[x+1][y-1] == 'X' and current_board[x-1][y+1] == 'X'):
                        current_quadrants[x/3][y/3] = 'X'
                        #print('c')
                        
            if (current_board[x][y] == 'O'):
                #check horizontal
                if (x%3 == 0 and current_board[x + 1][y] == 'O' and current_board[x+2][y] == 'O'):
                    current_quadrants[x/3][y/3] = 'O'
                    
                #check vertical
                if (y%3 == 0 and current_board[x][y+1] == 'O' and current_board[x][y+2] == 'O'):
                    current_quadrants[x/3][y/3] = 'O'
                    
                #check diagonal
                if (x%3 == 1 and y%3 == 1):
                    if (current_board[x-1][y-1] == 'O' and current_board[x+1][y+1] == 'O'):
                        current_quadrants[x/3][y/3] = 'O'
                    elif (current_board[x+1][y-1] == 'O' and current_board[x-1][y+1] == 'O'):
                        current_quadrants[x/3][y/3] = 'O'

###################user methods######################

def getMove(lastMove, token, current_board, current_quadrants):
    printboard(board)
    move = input("Next move? (Format row,column starting at 0)")
    while (not validMove(lastMove, move, current_board, current_quadrants)):
        move = input("Invalid move. Try again.")
    return move


##################computer methods##################

def getAllNextMoves(lastMove, newBoard, current_quadrants):
    potentialMoves = []
    for x in range(0,9):
        for y in range(0,9):
            if (validMove(lastMove, (x,y), newBoard, current_quadrants)):
                potentialMoves.append((x,y))
    return potentialMoves

def getComputerMove_naive():
    return (random.randint(0,8), random.randint(0,8))

def getComputerMove_hard(lastMove, computer, player, current_quadrants):
    q = Queue.Queue()
    potentialMoves = getAllNextMoves(lastMove, board, current_quadrants)
    for each in potentialMoves:
        new_board = copy.deepcopy(board)
        new_board[each[0]][each[1]] = computer
        new_quadrants = copy.deepcopy(current_quadrants)
        last_count = countQuadrants(current_quadrants, computer)
        updateQuadrants(new_quadrants, new_board)
        q.put((each, new_board, computer, each, new_quadrants, last_count))
    count = 1
    while (not q.empty()):
        count +=1
        leaf = q.get()
        if (count == 5000):
            return leaf[0]
        #print(leaf[0])
        #printboard(leaf[1])
        if (checkWin(leaf[1], computer, leaf[4])):
            return leaf[0]
        if (not checkWin(leaf[1], player, leaf[4])):
            if (leaf[5] < countQuadrants(leaf[4], player) and leaf[2] == player):
                if (leaf[5] < countQuadrants(leaf[4]) and leaf[2] == computer):
                    return leaf[0]
                potentialMoves = getAllNextMoves(leaf[3], leaf[1], leaf[4])
                for each in potentialMoves:
                    new_board = copy.deepcopy(leaf[1])
                    if (leaf[2] == computer):
                        new_board[each[0]][each[1]] = player
                        new_quadrants = copy.deepcopy(leaf[4])
                        last_count = countQuadrants(new_quadrants, computer)
                        updateQuadrants(new_quadrants, new_board)
                        q.put((leaf[0], new_board, player, each, new_quadrants, last_count))
                    else:
                        new_board[each[0]][each[1]] = computer
                        new_quadrants = copy.deepcopy(leaf[4])
                        last_count = countQuadrants(new_quadrants, player)
                        updateQuadrants(new_quadrants, new_board)
                        q.put((leaf[0], new_board, computer, each, new_quadrants, last_count))
    if (q.empty()):
        return getComputerMove_naive()
                
        
def countQuadrants(current_quadrants, token):
    count = 0
    for x in range(0,3):
        for y in range(0,3):
            if (current_quadrants[x][y] == token):
                count += 1
    return count
    

     

#################gameplay methods###################
  
def play():   
    print("Welcome to Tic-Tac-Tic-Tac-Toe!")

    token = raw_input("Do you want to be X or O? ")

    while (token != "X" and token != "O"):
        token = raw_input("Invalid option. Do you want to be X or O?")
    
    if (token != 'X'):
        computer = 'X'
    else:
        computer = 'O'

    computerMove = None
    while ( not checkWin(board, 'O', quadrants) and  not checkWin(board,'X', quadrants)):
        move = getMove(computerMove, token, board, quadrants)
        board[move[0]][move[1]] = token
        updateQuadrants(quadrants, board)
        if (checkWin(board, token, quadrants)):
            return token;
        if (cat(move, board, quadrants)):
            return 'C';
        
        printboard(board)
        #getComputerMove_hard(move, computer)
        computerMove = getComputerMove_naive()
        #computerMove = getComputerMove_hard(move, computer, token, quadrants)
        #print(validMove(move, computerMove, board))
        while(not validMove(move, computerMove, board)):
            computerMove = getComputerMove_naive()
        board[computerMove[0]][computerMove[1]] = computer
        updateQuadrants(quadrants, board)
        print("Computer went at position: " + str(computerMove))
        if (checkWin(board, computer, quadrants)):
            return computer;
        if (cat(computerMove, board, quadrants)):
            return 'C';
        
    

def main():
    winner = play()
    if (winner == 'C'):
        print("Cat! Nobody wins")
    else:
        print("Winner! " + str(winner) + " wins!")
      
########################################################
        
main()
#getComputerMove_hard((3,6), 'X', 'O')
        
        
        
        
        
        
        
        
        
        
#_|_|_ || _|_|_ || _|X|_
#_|_|_ || _|_|_ || _|_|_
# | |  ||  | |  ||  |O|
#========================
#_|_|_ || _|_|_ || _|_|_
#_|_|_ || _|_|_ || _|_|_
# | |  ||  | |  ||  | |
#========================
#_|_|_ || _|_|_ || _|_|_
#_|_|_ || _|_|_ || _|_|_
# | |  ||  | |  ||  | |
 
 
