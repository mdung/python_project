import numpy as np
import matplotlib.pyplot as plt

def distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

def nearest_neighbor(cities):
    num_cities = len(cities)
    unvisited_cities = set(range(1, num_cities))
    tour = [0]  # Starting from city 0

    while unvisited_cities:
        current_city = tour[-1]
        nearest_city = min(unvisited_cities, key=lambda city: distance(cities[current_city], cities[city]))
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)

    return tour

def total_distance(tour, cities):
    dist = 0
    for i in range(len(tour) - 1):
        dist += distance(cities[tour[i]], cities[tour[i + 1]])
    dist += distance(cities[tour[-1]], cities[tour[0]])  # Return to the starting city
    return dist

# Example: Randomly generate 10 cities
np.random.seed(42)
num_cities = 10
cities = np.random.rand(num_cities, 2)  # 2D coordinates

# Solve TSP using nearest neighbor algorithm
tour = nearest_neighbor(cities)

# Visualize the result
x = cities[:, 0]
y = cities[:, 1]

plt.scatter(x, y, c='blue', marker='o', label='Cities')
plt.plot(x[tour + [tour[0]]], y[tour + [tour[0]]], c='red', linestyle='-', linewidth=2, label='Tour')
plt.title(f'TSP Solution (Total Distance: {total_distance(tour, cities):.4f})')
plt.legend()
plt.show()
