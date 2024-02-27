debug = False
mode = 3


def printBoard(moves):
    board = [["_"] * 3 for _ in range(3)]

    turn = "A"
    for c, r in moves:
        if turn == "A":
            board[2 - r][c] = "X"
            turn = "B"
        else:
            board[2 - r][c] = "O"
            turn = "A"

    for i in range(3):
        print(board[i])


def tictactoe(moves: list[list[int]]) -> str:
    board = [[""] * 3 for _ in range(3)]
    symbolToWinner = {"X": "A", "O": "B"}

    turn = "A"
    for c, r in moves:
        if turn == "A":
            board[2 - r][c] = "X"
            turn = "B"
        else:
            board[2 - r][c] = "O"
            turn = "A"

    for i in range(3):
        if board[i] == ["X", "X", "X"]:
            return "A"
        elif board[i] == ["O", "O", "O"]:
            return "B"

    for s, w in symbolToWinner.items():
        for j in range(3):
            for i in range(3):
                if board[i][j] != s:
                    break
            else:
                return w

    for s, w in symbolToWinner.items():
        for i, j in [[0, 0], [1, 1], [2, 2]]:
            if board[i][j] != s:
                break
        else:
            return w

    for s, w in symbolToWinner.items():
        for i, j in [[0, 2], [1, 1], [2, 0]]:
            if board[i][j] != s:
                break
        else:
            return w

    return "Draw" if len(moves) == 9 else "Pending"


def printBoard4(moves):
    board = [["_"] * 4 for _ in range(4)]

    turn = "A"
    for c, r in moves:
        if turn == "A":
            board[3 - r][c] = "X"
            turn = "B"
        else:
            board[3 - r][c] = "O"
            turn = "A"

    for i in range(4):
        print(board[i])


def tictactoe4(moves):
    board = [[""] * 4 for _ in range(4)]
    symbolToWinner = {"X": "A", "O": "B"}

    turn = "A"
    for c, r in moves:
        if turn == "A":
            board[3 - r][c] = "X"
            turn = "B"
        else:
            board[3 - r][c] = "O"
            turn = "A"

    for i in range(4):
        if board[i] == ["X", "X", "X"]:
            return "A"
        elif board[i] == ["O", "O", "O"]:
            return "B"

    for s, w in symbolToWinner.items():
        for j in range(4):
            for i in range(4):
                if board[i][j] != s:
                    break
            else:
                return w

    for s, w in symbolToWinner.items():
        for i, j in [[0, 0], [1, 1], [2, 2], [3, 3]]:
            if board[i][j] != s:
                break
        else:
            return w

    for s, w in symbolToWinner.items():
        for i, j in [[0, 3], [1, 2], [2, 1], [3, 0]]:
            if board[i][j] != s:
                break
        else:
            return w

    return "Draw" if len(moves) == 16 else "Pending"


def printBoard5(moves):
    board = [["_"] * 5 for _ in range(5)]

    turn = "A"
    for c, r in moves:
        if turn == "A":
            board[4 - r][c] = "X"
            turn = "B"
        else:
            board[4 - r][c] = "O"
            turn = "A"

    for i in range(5):
        print(board[i])


def tictactoe5(moves):
    board = [[""] * 5 for _ in range(5)]
    symbolToWinner = {"X": "A", "O": "B"}

    turn = "A"
    for c, r in moves:
        if turn == "A":
            board[4 - r][c] = "X"
            turn = "B"
        else:
            board[4 - r][c] = "O"
            turn = "A"

    for i in range(5):
        if board[i] == ["X", "X", "X"]:
            return "A"
        elif board[i] == ["O", "O", "O"]:
            return "B"

    for s, w in symbolToWinner.items():
        for j in range(5):
            for i in range(5):
                if board[i][j] != s:
                    break
            else:
                return w

    for s, w in symbolToWinner.items():
        for i, j in [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]:
            if board[i][j] != s:
                break
        else:
            return w

    for s, w in symbolToWinner.items():
        for i, j in [[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]]:
            if board[i][j] != s:
                break
        else:
            return w

    return "Draw" if len(moves) == 25 else "Pending"


def main():
    moves = []

    if mode == 5:
        legalPositions = {"0", "1", "2", "3", "4"}
    elif mode == 4:
        legalPositions = {"0", "1", "2", "3"}
    else:
        legalPositions = {"0", "1", "2"}

    turn = "A"
    while True:
        if turn == "A":
            userInput = input(
                "Player A's turn. Enter a move (\"<x-coordinate> <y-coordinate>\"): ")
        else:
            userInput = input(
                "Player B's turn. Enter a move (\"<x-coordinate> <y-coordinate>\"): ")

        userInput = userInput.rstrip().lstrip()

        if len(userInput) != 3 or userInput[0] not in legalPositions or userInput[1] != " " or userInput[2] not in legalPositions:
            print("Illegal move\n")
            continue

        move = (int(userInput[0]), int(userInput[2]))
        if move in moves:
            print("You already placed a symbol there.\n")
            continue
        else:
            moves.append(move)

        if turn == "A":
            turn = "B"
        else:
            turn = "A"

        if mode == 5:
            printBoard5(moves)
        elif mode == 4:
            printBoard4(moves)
        else:
            printBoard(moves)
        print()

        if mode == 5:
            winner = tictactoe5(moves)
        elif mode == 4:
            winner = tictactoe4(moves)
        else:
            winner = tictactoe(moves)

        match winner:
            case "A":
                print("A wins.")
                break
            case "B":
                print("B wins.")
                break
            case "Draw":
                print("It's a draw.")
                break

    if debug:
        print(moves)


if __name__ == "__main__":
    main()
