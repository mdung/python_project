import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class GeneticAlgorithmOptimizer:
    def __init__(self, target_function, population_size, generations, crossover_rate, mutation_rate):
        self.target_function = target_function
        self.population_size = population_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.best_solution = None
        self.best_fitness = float('-inf')
        self.population = []

    def initialize_population(self):
        self.population = np.random.rand(self.population_size)

    def evaluate_population(self):
        fitness_values = [self.target_function(individual) for individual in self.population]
        best_index = np.argmax(fitness_values)
        current_best_fitness = fitness_values[best_index]
        if current_best_fitness > self.best_fitness:
            self.best_fitness = current_best_fitness
            self.best_solution = self.population[best_index]

    def select_parents(self):
        sorted_indices = np.argsort([self.target_function(individual) for individual in self.population])[::-1]
        selected_indices = sorted_indices[:int(self.crossover_rate * self.population_size)]
        return self.population[selected_indices]

    def crossover(self, parents):
        crossover_point = np.random.randint(1, len(parents[0]))
        child = np.concatenate((parents[0][:crossover_point], parents[1][crossover_point:]))
        return child

    def mutate(self, child):
        mutation_point = np.random.randint(len(child))
        child[mutation_point] += np.random.normal(0, 0.1)
        return child

    def run_genetic_algorithm(self):
        self.initialize_population()
        for generation in range(self.generations):
            self.evaluate_population()
            parents = self.select_parents()
            offspring = []

            for i in range(0, len(parents), 2):
                if i + 1 < len(parents):
                    child = self.crossover([parents[i], parents[i + 1]])
                    child = self.mutate(child)
                    offspring.append(child)

            self.population[:len(offspring)] = offspring

        self.evaluate_population()

class GeneticAlgorithmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Genetic Algorithm Optimization")
        self.root.geometry("800x600")

        self.target_function_label = ttk.Label(self.root, text="Target Function:")
        self.target_function_label.grid(row=0, column=0, padx=10, pady=10)

        self.target_function_entry = ttk.Entry(self.root)
        self.target_function_entry.grid(row=0, column=1, padx=10, pady=10)

        self.run_button = ttk.Button(self.root, text="Run Genetic Algorithm", command=self.run_genetic_algorithm)
        self.run_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.plot_frame = ttk.Frame(self.root)
        self.plot_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def run_genetic_algorithm(self):
        target_function_str = self.target_function_entry.get()
        target_function = lambda x: eval(target_function_str, {"x": x})

        optimizer = GeneticAlgorithmOptimizer(target_function=target_function,
                                              population_size=100,
                                              generations=50,
                                              crossover_rate=0.5,
                                              mutation_rate=0.1)

        optimizer.run_genetic_algorithm()

        x_values = np.linspace(0, 1, 100)
        y_values = [target_function(x) for x in x_values]

        fig, ax = plt.subplots()
        ax.plot(x_values, y_values, label="Target Function")
        ax.axvline(optimizer.best_solution, color='r', linestyle='--', label='Optimal Solution')

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = ttk.Frame(self.plot_frame)
        toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar.update()

        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        canvas.tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = GeneticAlgorithmApp(root)
    root.mainloop()
