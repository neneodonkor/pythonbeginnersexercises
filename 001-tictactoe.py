# This is a sample Python script.

import random

if __name__ == '__main__':
    print("\n")
    print("Python Workouts!")
    print("------------------------------")

# Tic-tac-toe input
#
# The tic-tac-toe board looks like this:
#
# 1:  X | O | X
#    -----------
# 2:    |   |
#    -----------
# 3:  O |   |
#
#     A   B  C
#
# The board is represented as a 2D list:
#
# board = [
#     [" ", " ", " ", "1"],
#     [" ", " ", " ", "2"],
#     [" ", " ", " ", "3"],
#     ["A", "B", "C"]
# ]
#


# ----------------------------------------------------------

# The dictionary to represent the cell name, its position,
# and whether it is empty or filled.
tictactoe = {
    'A1': [(0, 0), 'EMPTY'],
    'A2': [(1, 0), 'EMPTY'],
    'A3': [(2, 0), 'EMPTY'],
    'B1': [(0, 1), 'EMPTY'],
    'B2': [(1, 1), 'EMPTY'],
    'B3': [(2, 1), 'EMPTY'],
    'C1': [(0, 2), 'EMPTY'],
    'C2': [(1, 2), 'EMPTY'],
    'C3': [(2, 2), 'EMPTY']
}

board = [
    [" ", " ", " ", "1"],
    [" ", " ", " ", "2"],
    [" ", " ", " ", "3"],
    ["A", "B", "C"]
]

print("To play the game select any of the cells on the board.")
print("Available cells are: A1, A2, A3, B1, B2, B3, C1, C2, and C3.\n")


# ----------------------------------------------------------


# This is to print the board to the screen.
def printBoard() -> None:
    print("")
    for idx in range(4):
        print(board[idx], end="\n")
    print("")


printBoard()

# ----------------------------------------------------------

# Randomize which player gets 'X' or 'O'
XO = ['X', 'O']
tictac = random.choice(XO)
player1 = tictac
player2 = ''
for value in XO:
    if tictac != value:
        player2 = value

print(f"Player 1 is {player1}\nPlayer 2 is {player2}\n")


# ----------------------------------------------------------


# This to check if any of the cells are 'FILLED' and line up
# horintally, vertically, and diagonally.
def checkWin(player) -> bool | str:
    if tictactoe['A1'][1] == 'FILLED':
        if board[0][0] == board[1][0] == board[2][0]:
            # A1 == A2 == A3
            print(f"Player {player} has won the game")
            return True
        elif board[0][0] == board[0][1] == board[0][2]:
            # A1 == B1 == C1
            print(f"Player {player} has won the game")
            return True
        elif board[0][0] == board[1][1] == board[2][2]:
            # A1 == B2 == C3
            print(f"Player {player} has won the game")
            return True

    if tictactoe['B1'][1] == 'FILLED':
        if board[0][1] == board[1][1] == board[2][1]:
            # B1 == B2 == B3
            print(f"Player {player} has won the game")
            return True

    if tictactoe['C1'][1] == 'FILLED':
        if board[0][2] == board[1][2] == board[2][2]:
            # C1 == C2 == C3
            print(f"Player {player} has won the game")
            return True
        elif board[0][2] == board[1][1] == board[2][0]:
            # C1 == B2 == A3
            print(f"Player {player} has won the game")
            return True

    if tictactoe['A2'][1] == 'FILLED':
        if board[1][0] == board[1][1] == board[1][2]:
            # A2 == B2 == C2
            print(f"Player {player} has won the game")
            return True

    if tictactoe['A3'][1] == 'FILLED':
        if board[2][0] == board[2][1] == board[2][2]:
            # A3 == B3 == C3
            print(f"Player {player} has won the game")
            return True

    # If there is no winner, the game ends in a draw when
    # all the cells are filled.
    filled = [val[1] for val in tictactoe.values() if val[1] == 'FILLED']
    if len(filled) == 9:
        return "DRAW"

    return False


# ----------------------------------------------------------


# The logic for the game play.
def gamePlay(player: int):
    xo = ''
    if player == 1:
        xo = player1
    elif player == 2:
        xo = player2

    # Get cell position to mark from player. Example: A1
    target = input(f"Player {player} [{xo}] choose a cell on the board: ").upper()

    # This is to check if the input is not outside what
    # is defined in the tictactoe dictionary. If 'EXIT' is
    # typed, then the game ends. If the right input is
    # entered, the function returns the cell chosen.
    def checkInput(text: str) -> str:
        if text == "EXIT":
            print("You quit the game!")
            return text

        while True:
            for key in tictactoe.keys():
                if text == key:
                    return text

            print(f"This is not a valid input. Please try again!\n")
            text = input(f"Player {player} [{xo}] choose a cell on the board: ").upper()

    # This is to pass along the correct input.
    target = checkInput(target)
    if target == 'EXIT':
        return target

    # Once the cell or key is chosen from the dictionary,
    # the value of the key is unpacked: [tuple, _].
    # Position refers to the tuple, and _ refers to
    # the value 'EMPTY' or 'FILLED'
    position, _ = tictactoe.get(target)

    if tictactoe[target][1] == "FILLED":
        print("Cell is already filled!\n")
        target = input(f"Player {player} [{xo}] choose a cell on the board: ").upper()
        target = checkInput(target)
        position, _ = tictactoe.get(target)

    if tictactoe[target][1] == "EMPTY":
        # Unpack the tuple to get row and column on
        # the board. This helps to mark a cell.
        row, column = position

        # Mark either 'X' or 'O' on board if the cell is
        # 'EMPTY'. Variables 'player1' or 'player2' will
        # either be 'X' or 'O'.
        if player == 1 and tictactoe[target][1] == 'EMPTY':
            board[row][column] = player1
            tictactoe[target][1] = 'FILLED'
        elif player == 2 and tictactoe[target][1] == 'EMPTY':
            board[row][column] = player2
            tictactoe[target][1] = 'FILLED'

    printBoard()
    print("-----------------------------------------------")

    # The 'checkWin()' checks if a player has won, or the
    # game ends in a draw. The variable 'wingame' has 3
    # states: True, False, or 'DRAW'.
    wingame: bool | str = checkWin(player)

    if wingame is True:
        print(f"Game Over! Player {player} wins!")
        return 'EXIT'
    elif wingame == 'DRAW':
        print("Game ends in a draw!")
        return 'EXIT'


# ----------------------------------------------------------

# This is to alternate between Player 1 and Player 2
win: bool = False
player_turn: int = 1

while True:
    if player_turn == 1:
        p = gamePlay(player_turn)
        if p == 'EXIT':
            break
        player_turn = 2

        if win:
            break

    elif player_turn == 2:
        p = gamePlay(player_turn)
        if p == 'EXIT':
            break
        player_turn = 1

        if win:
            break
