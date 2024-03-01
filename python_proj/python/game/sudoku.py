def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-"*21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

def is_valid(board, row, col, num):
    # Check if the number is not in the current row or column
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number is not in the current 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(board):
    empty_row, empty_col = find_empty(board)

    if empty_row is None and empty_col is None:
        return True  # The board is solved

    for num in range(1, 10):
        if is_valid(board, empty_row, empty_col, num):
            board[empty_row][empty_col] = num

            if solve_sudoku(board):
                return True  # Successfully solved

            board[empty_row][empty_col] = 0  # Backtrack if the solution is not valid

    return False  # No valid solution found

def create_puzzle():
    # You can customize this function to generate different puzzles
    pass

def main():
    # Initialize an empty 9x9 Sudoku board
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Sudoku Puzzle:")
    print_board(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku:")
        print_board(sudoku_board)
    else:
        print("\nNo solution exists.")

if __name__ == "__main__":
    main()
