debug = False


def tictactoe(moves: list[list[int]]) -> str:
    board = [[""] * 3 for _ in range(3)]
    symbolToWinner = {"X": "A", "O": "B"}

    turn = "A"
    for r, c in moves:
        if turn == "A":
            board[r][c] = "X"
            turn = "B"
        else:
            board[r][c] = "O"
            turn = "A"

    for i in range(3):
        print(board[i])

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


def main():
    moves = []
    legalPositions = ["0", "1", "2"]
    numMoves = 0
    turn = "A"

    while numMoves < 9:
        if turn == "A":
            userInput = input(
                "Player A's turn. Enter a move (\"<position1> <position2>\") or type \"done\" if you are finished entering moves: ")
            turn = "B"
        else:
            userInput = input(
                "Player B's turn. Enter a move (\"<position1> <position2>\") or type \"done\" if you are finished entering moves: ")
            turn = "A"

        userInput = userInput.rstrip()

        if userInput == "done":
            if not moves:
                print("Please enter at least one move")
                continue
            else:
                break

        if len(userInput) != 3 or userInput[0] not in legalPositions or userInput[1] != " " or userInput[2] not in legalPositions:
            print("Illegal move")
            continue

        move = (int(userInput[0]), int(userInput[2]))
        if move in moves:
            print("You already added that move.")
            continue
        else:
            moves.append(move)
        numMoves += 1

        if debug:
            print(numMoves)

    if debug:
        print(moves)

    print(tictactoe(list(moves)))


if __name__ == "__main__":
    main()
