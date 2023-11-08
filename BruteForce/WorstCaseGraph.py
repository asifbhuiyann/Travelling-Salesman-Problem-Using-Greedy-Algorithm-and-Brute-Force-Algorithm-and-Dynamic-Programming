import random
import timeit
import matplotlib.pyplot as plt
from itertools import permutations


# Function to generate a worst-case distance matrix for n cities
def generate_worst_case_distances(n):
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = 100  # Set a high distance between all pairs of cities
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


# Calculate the worst-case distance for the worst case
def calculate_worst_distance(algorithm, num_cities):
    distances = generate_worst_case_distances(num_cities)
    min_distance, _ = algorithm(distances)
    return min_distance


# Number of cities for the worst case
num_cities_list = [3, 4, 5, 6]  # You can adjust this as needed

# Initialize a list to store the worst-case distances for Brute Force
worst_distances_brute_force = []

# Calculate worst-case distances for Brute Force Algorithm
for num_cities in num_cities_list:
    worst_distance_brute_force = calculate_worst_distance(tsp_brute_force, num_cities)
    worst_distances_brute_force.append(worst_distance_brute_force)

# Create a graph to visualize the worst-case distances for Brute Force Algorithm
plt.figure(figsize=(10, 6))
plt.plot(num_cities_list, worst_distances_brute_force, marker='o', label='Brute Force')
plt.xlabel('Number of Cities')
plt.ylabel('Worst-Case Distance')
plt.title('Worst-Case Distance for Brute Force Algorithm')
plt.legend()
plt.grid()
plt.show()
