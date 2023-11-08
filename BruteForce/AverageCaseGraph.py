import random
import timeit
import matplotlib.pyplot as plt
from itertools import permutations


# Function to generate random distance matrix for n cities
def generate_random_distances(n):
    distances = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)  # Distance from a city to itself is 0
            else:
                row.append(random.randint(1, 100))  # Random distance between 1 and 100
        distances.append(row)
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


# Calculate the average distance for the average case
def calculate_average_distance(algorithm, num_cities, num_runs):
    total_distance = 0
    for _ in range(num_runs):
        distances = generate_random_distances(num_cities)
        min_distance, _ = algorithm(distances)
        total_distance += min_distance
    return total_distance / num_runs


# Number of cities and runs for the average case
num_cities_list = [5, 10, 15, 20, 25]  # You can adjust this as needed
num_runs = 5  # Number of runs for each case

# Initialize a list to store the average distances for Brute Force
average_distances_brute_force = []

# Calculate average distances for Brute Force Algorithm
for num_cities in num_cities_list:
    average_distance_brute_force = calculate_average_distance(tsp_brute_force, num_cities, num_runs)
    average_distances_brute_force.append(average_distance_brute_force)

# Create a graph to visualize the average distances for Brute Force Algorithm
plt.figure(figsize=(10, 6))
plt.plot(num_cities_list, average_distances_brute_force, marker='o', label='Brute Force')
plt.xlabel('Number of Cities')
plt.ylabel('Average Distance')
plt.title('Average Distance for Brute Force Algorithm')
plt.legend()
plt.grid()
plt.show()
