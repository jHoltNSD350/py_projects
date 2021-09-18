#Tic Tac Toe game in python: Courtesy of Tech With Tim
import os
from sys import platform

board: list = [' ' for x in range(10)]

def insertLetter(letter: str, pos: int) -> None:
    board[pos] = letter

def spaceIsFree(pos: int) -> bool:
    return board[pos] == ' '

def printBoard(board: list) -> None:
    if platform == 'linux':
        os.system('clear')
    elif playform == 'win32':
        os.system('cls')

    print('   |   |')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print('   |   |')

def isWinner(bo: list, le: str) -> bool:
    return  check_win(le, 7, 8, 9) or \
            check_win(le, 4, 5, 6) or \
            check_win(le, 1, 2, 3) or \
            check_win(le, 1, 4, 7) or \
            check_win(le, 2, 5, 8) or \
            check_win(le, 3, 6, 9) or \
            check_win(le, 1, 5, 9) or \
            check_win(le, 3, 5, 7)

def check_win(player: str, p1: int, p2: int, p3: int) -> bool:
    return board[p1] == player and board[p2] == player and board[p3] == player

def playerMove():
    run: bool = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number')

def compMove() -> int:
    possibleMoves: list = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move: int = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy: list = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen: list = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen: list = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    return move

def selectRandom(li: list) -> int:
    import random
    ln: int = len(li)
    r: int = random.randrange(0, ln)
    return li[r]

def isBoardFull(board: list) -> bool:
    return board.count(' ') <= 1

def main():
    print('Welcome to Tic Tac Toe')
    printBoard(board)

    while not isBoardFull(board):
        if not isWinner(board, 'O'):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not isWinner(board, 'X'):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print(f'Computer placed an \'O\' in position {move}:')
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break


    if isBoardFull(board):
        print('Tie Game!')

if __name__ == '__main__':
    main()
# TODO fix bot logic
