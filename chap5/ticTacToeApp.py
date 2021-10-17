import os

def clearScreen():
    os.system('clear')

def header():
    print()
    print(" ******   **   ****        ******    ****     ****         ******    ****    ****")
    print("   **     **  *       ++     **     * __ *   *       ++      **     *    *  **__")
    print("   **     **  *       ++     **     *    *   *       ++      **     *    *  **")
    print("   **     **   ****          **     *    *    ****           **      ****    ****")
    print()

theBoard = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5:
' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

availableList = list(theBoard.keys())
i = 1

def printBoard(board):
    header()
    print()
    print("\t\t\t\t" + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('\t\t\t\t---+-----+---')
    print("\t\t\t\t" + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('\t\t\t\t---+-----+---')
    print("\t\t\t\t" + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print()

def log(message):
    separator = '--------------------------------------------------------------------'
    printBoard(theBoard)
    print()
    print(separator)
    print(message)
    print(separator)
    print()



def listAvailablePlaces():
    availableList.clear()
    for k, v in theBoard.items():
        if v == ' ':
            availableList.append(k)

def someoneWon():
    if (theBoard[1] == 'X' and theBoard[2] == 'X' and theBoard[3] == 'X') \
    or (theBoard[4] == 'X' and theBoard[5] == 'X' and theBoard[6] == 'X') \
    or (theBoard[7] == 'X' and theBoard[8] == 'X' and theBoard[9] == 'X') \
    or (theBoard[1] == 'X' and theBoard[5] == 'X' and theBoard[9] == 'X') \
    or (theBoard[1] == 'X' and theBoard[4] == 'X' and theBoard[7] == 'X') \
    or (theBoard[2] == 'X' and theBoard[5] == 'X' and theBoard[8] == 'X') \
    or (theBoard[3] == 'X' and theBoard[6] == 'X' and theBoard[9] == 'X') \
    or (theBoard[3] == 'X' and theBoard[5] == 'X' and theBoard[7] == 'X'):
        return True
    elif (theBoard[1] == 'O' and theBoard[2] == 'O' and theBoard[3] == 'O') \
    or (theBoard[4] == 'O' and theBoard[5] == 'O' and theBoard[6] == 'O') \
    or (theBoard[7] == 'O' and theBoard[8] == 'O' and theBoard[9] == 'O') \
    or (theBoard[1] == 'O' and theBoard[5] == 'O' and theBoard[9] == 'O') \
    or (theBoard[1] == 'O' and theBoard[4] == 'O' and theBoard[7] == 'O') \
    or (theBoard[2] == 'O' and theBoard[5] == 'O' and theBoard[8] == 'O') \
    or (theBoard[3] == 'O' and theBoard[6] == 'O' and theBoard[9] == 'O') \
    or (theBoard[3] == 'O' and theBoard[5] == 'O' and theBoard[7] == 'O'):
        return True
    else:
        return False


turn = 'X'
#for i in range(9):
while i <= 9:
    listAvailablePlaces()
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
        
    while True:
        try:
            move = int(input())
            if move < 1 or move > 9:
                raise KeyError
            break
        except ValueError:
            clearScreen()
            #print(f"Please type a number. Options available {availableList}")
            log(f"Please type a number. Options available {availableList}.\n==> Turn for {turn}")
        except KeyError:
            clearScreen()
            #print(f"Please type a number between 1 and 9. \n\t Options available {availableList}")
            log(f"Invalid input\nType a number between 1 and 9, please.\nOptions available {availableList}.\n==> Turn for {turn}")
    
    if theBoard[move] == 'X' or theBoard[move] == 'O':
        #print("This place is already in use")
        clearScreen()
        log(f"This place { {move} } is already in use. Options available {availableList}.\n==> Turn for {turn}")
    else:
        theBoard[move] = turn

        if someoneWon():
            log(f"WOW...we have a winner. Congratulation 'Player {turn}' ")
            break
        elif someoneWon() == False and i == 9:
            log("Ohhhhh what a pity. We have a TIE result")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        i = i + 1
printBoard(theBoard)
