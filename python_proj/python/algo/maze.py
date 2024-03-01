import tkinter as tk
import heapq

class MazeSolver(tk.Tk):
    def __init__(self, maze):
        super().__init__()

        self.title("Maze Solver")
        self.geometry("400x400")

        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])

        self.canvas = tk.Canvas(self, width=400, height=400, bg="white")
        self.canvas.pack()

        self.draw_maze()
        self.solve_maze()

    def draw_maze(self):
        cell_width = 400 / self.cols
        cell_height = 400 / self.rows

        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == 1:
                    self.canvas.create_rectangle(
                        j * cell_width, i * cell_height,
                        (j + 1) * cell_width, (i + 1) * cell_height,
                        fill="black"
                    )

    def solve_maze(self):
        start = (0, 0)
        end = (self.rows - 1, self.cols - 1)

        path = self.astar(start, end)
        self.draw_path(path)

    def astar(self, start, end):
        heap = [(0, start)]
        visited = set()
        parent = {}

        while heap:
            current_cost, current_node = heapq.heappop(heap)

            if current_node == end:
                path = []
                while current_node in parent:
                    path.insert(0, current_node)
                    current_node = parent[current_node]
                path.insert(0, start)
                return path

            if current_node in visited:
                continue

            visited.add(current_node)

            for neighbor in self.get_neighbors(current_node):
                cost = current_cost + 1 + self.heuristic(neighbor, end)

                heapq.heappush(heap, (cost, neighbor))
                parent[neighbor] = current_node

        return []

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(self, node):
        neighbors = []
        x, y = node

        if x > 0 and self.maze[x - 1][y] != 1:
            neighbors.append((x - 1, y))
        if x < self.rows - 1 and self.maze[x + 1][y] != 1:
            neighbors.append((x + 1, y))
        if y > 0 and self.maze[x][y - 1] != 1:
            neighbors.append((x, y - 1))
        if y < self.cols - 1 and self.maze[x][y + 1] != 1:
            neighbors.append((x, y + 1))

        return neighbors

    def draw_path(self, path):
        cell_width = 400 / self.cols
        cell_height = 400 / self.rows

        for node in path:
            x, y = node
            self.canvas.create_rectangle(
                y * cell_width, x * cell_height,
                (y + 1) * cell_width, (x + 1) * cell_height,
                fill="green"
            )

if __name__ == "__main__":
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]

    maze_solver = MazeSolver(maze)
    maze_solver.mainloop()
