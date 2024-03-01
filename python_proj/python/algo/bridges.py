import tkinter as tk
from tkinter import ttk, Canvas, messagebox
import networkx as nx
from networkx.algorithms import articulation_points, bridges

class GraphAnalyzerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Graph Analyzer")

        self.canvas = Canvas(master, width=800, height=600, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.analyze_button = ttk.Button(master, text="Analyze Graph", command=self.analyze_graph)
        self.analyze_button.pack(pady=10)

        # Example graph (you can replace this with your own graph)
        self.graph = nx.Graph()
        self.graph.add_edges_from([(1, 2), (2, 3), (2, 4), (3, 5), (4, 5), (4, 6), (6, 7), (7, 8)])

    def draw_graph(self):
        pos = nx.spring_layout(self.graph)
        nx.draw_networkx(self.graph, pos, with_labels=True, ax=self.canvas)

    def highlight_articulation_points(self):
        articulation_nodes = articulation_points(self.graph)
        self.draw_highlighted_nodes(articulation_nodes, "red")

    def highlight_bridges(self):
        bridge_edges = bridges(self.graph)
        self.draw_highlighted_edges(bridge_edges, "blue")

    def draw_highlighted_nodes(self, nodes, color):
        pos = nx.spring_layout(self.graph)
        nx.draw_networkx_nodes(self.graph, pos, nodelist=nodes, node_color=color, ax=self.canvas)

    def draw_highlighted_edges(self, edges, color):
        pos = nx.spring_layout(self.graph)
        nx.draw_networkx_edges(self.graph, pos, edgelist=edges, edge_color=color, ax=self.canvas)

    def analyze_graph(self):
        self.draw_graph()
        self.highlight_articulation_points()
        self.highlight_bridges()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphAnalyzerApp(root)
    root.mainloop()
