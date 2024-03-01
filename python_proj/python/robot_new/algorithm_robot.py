import tkinter as tk
import heapq

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

def astar(maze, start, end):
    open_set = []
    closed_set = set()
    heapq.heappush(open_set, (0, start))

    while open_set:
        current_cost, current_node = heapq.heappop(open_set)
        current = current_node.position

        if current == end:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current)

        for neighbor in get_neighbors(maze, current):
            if neighbor in closed_set:
                continue

            tentative_g = current_node.g + 1
            if neighbor not in [i[1].position for i in open_set] or tentative_g < neighbor.g:
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor.position, end)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current_node
                heapq.heappush(open_set, (neighbor.f, neighbor))

    return None

def get_neighbors(maze, pos):
    neighbors = []
    for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        new_pos = (pos[0] + move[0], pos[1] + move[1])
        if 0 <= new_pos[0] < len(maze) and 0 <= new_pos[1] < len(maze[0]) and maze[new_pos[0]][new_pos[1]] != 1:
            neighbors.append(Node(position=new_pos))
    return neighbors

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

class RobotPathApp:
    def __init__(self, master, width, height):
        self.master = master
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(master, width=width, height=height)
        self.canvas.pack()
        self.maze = [[0] * width for _ in range(height)]
        self.start = (0, 0)
        self.end = (width - 1, height - 1)

        self.draw_grid()
        self.draw_obstacles()

    def draw_grid(self):
        for i in range(0, self.width, 20):
            self.canvas.create_line(i, 0, i, self.height, fill="gray", dash=(2, 2))
        for j in range(0, self.height, 20):
            self.canvas.create_line(0, j, self.width, j, fill="gray", dash=(2, 2))

    def draw_obstacles(self):
        # Place obstacles in the maze (1 represents an obstacle)
        obstacle_positions = [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1),
                              (6, 2), (6, 3), (6, 4), (5, 4), (4, 4),
                              (3, 4), (3, 3), (3, 2), (8, 6), (8, 7),
                              (8, 8), (7, 8), (6, 8), (5, 8), (4, 8)]
        for pos in obstacle_positions:
            self.maze[pos[1]][pos[0]] = 1
            self.canvas.create_rectangle(pos[0] * 20, pos[1] * 20, (pos[0] + 1) * 20, (pos[1] + 1) * 20, fill="black")

    def visualize_path(self):
        path = astar(self.maze, Node(position=self.start), Node(position=self.end))
        if path:
            for pos in path:
                x, y = pos
                self.canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="green")
        else:
            print("No path found!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Robot Path Planning Visualization")
    app = RobotPathApp(root, width=400, height=300)
    app.visualize_path()
    root.mainloop()
