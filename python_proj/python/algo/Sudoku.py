import tkinter as tk

class SudokuSolver(tk.Tk):
    def __init__(self, puzzle):
        super().__init__()

        self.title("Sudoku Solver")
        self.geometry("400x400")

        self.puzzle = puzzle

        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.load_board()

        self.solve_button = tk.Button(self, text="Solve", command=self.solve_sudoku)
        self.solve_button.pack(pady=10)

    def load_board(self):
        for i in range(9):
            for j in range(9):
                value = self.puzzle[i][j]
                if value != 0:
                    label = tk.Label(self, text=str(value), width=4, height=2, relief="solid")
                else:
                    label = tk.Entry(self, width=4, justify="center")
                label.grid(row=i, column=j)
                self.board[i][j] = label

    def solve_sudoku(self):
        if self.solve():
            tk.messagebox.showinfo("Sudoku Solver", "Sudoku solved successfully!")
        else:
            tk.messagebox.showinfo("Sudoku Solver", "No solution exists for the given puzzle.")

    def solve(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True

        row, col = empty_cell

        for num in range(1, 10):
            if self.is_valid(num, row, col):
                self.puzzle[row][col] = num
                self.board[row][col].config(text=str(num))
                self.update()
                if self.solve():
                    return True

                self.puzzle[row][col] = 0
                self.board[row][col].delete(0, tk.END)
                self.update()

        return False

    def find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == 0:
                    return i, j
        return None

    def is_valid(self, num, row, col):
        return (
                not self.used_in_row(num, row) and
                not self.used_in_col(num, col) and
                not self.used_in_box(num, row - row % 3, col - col % 3)
        )

    def used_in_row(self, num, row):
        return num in self.puzzle[row]

    def used_in_col(self, num, col):
        return num in [self.puzzle[i][col] for i in range(9)]

    def used_in_box(self, num, start_row, start_col):
        return any(
            num == self.puzzle[i][j]
            for i in range(start_row, start_row + 3)
            for j in range(start_col, start_col + 3)
        )

if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells)
    puzzle = [
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

    sudoku_solver = SudokuSolver(puzzle)
    sudoku_solver.mainloop()
