import random
import timeit
import matplotlib.pyplot as plt
from itertools import permutations


# Function to generate a best-case distance matrix for n cities
def generate_best_case_distances(n):
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distances[i][j] = j - i  # Nearest unvisited city is always the next city
            distances[j][i] = distances[i][j]
    return distances


# Brute Force Algorithm
def tsp_brute_force(distances):
    n = len(distances)
    min_distance = float('inf')
    min_path = []

    for path in permutations(range(n)):
        total_distance = 0
        for i in range(n - 1):
            total_distance += distances[path[i]][path[i + 1]]
        total_distance += distances[path[-1]][path[0]]  # Return to the starting city
        if total_distance < min_distance:
            min_distance = total_distance
            min_path = list(path)

    return min_distance, min_path


# Calculate the best-case distance for the best case
def calculate_best_distance(algorithm, num_cities, num_runs):
    total_distance = 0
    for _ in range(num_runs):
        distances = generate_best_case_distances(num_cities)
        min_distance, _ = algorithm(distances)
        total_distance += min_distance
    return total_distance / num_runs


# Number of cities and runs for the best case
num_cities_list = [5, 10, 15, 20, 25]  # You can adjust this as needed
num_runs = 5  # Number of runs for each case

# Initialize a list to store the best-case distances for Brute Force
best_distances_brute_force = []

# Calculate best-case distances for Brute Force Algorithm
for num_cities in num_cities_list:
    best_distance_brute_force = calculate_best_distance(tsp_brute_force, num_cities, num_runs)
    best_distances_brute_force.append(best_distance_brute_force)

# Create a graph to visualize the best-case distances for Brute Force Algorithm
plt.figure(figsize=(10, 6))
plt.plot(num_cities_list, best_distances_brute_force, marker='o', label='Brute Force')
plt.xlabel('Number of Cities')
plt.ylabel('Best-Case Distance')
plt.title('Best-Case Distance for Brute Force Algorithm')
plt.legend()
plt.grid()
plt.show()
