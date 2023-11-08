import random
import time
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
    min_path = float('inf')
    for perm in permutations(range(n)):
        current_distance = 0
        for i in range(n - 1):
            current_distance += distances[perm[i]][perm[i+1]]
        current_distance += distances[perm[-1]][perm[0]]
        min_path = min(min_path, current_distance)
    return min_path

# Number of cities and runs for the average case
num_cities = 5  # You can adjust this as needed
num_runs = 10   # Number of runs to calculate the average

# Generate random distances and calculate the execution time for Brute Force
start_time = time.perf_counter()  # Record the start time
total_distance = 0
for _ in range(num_runs):
    distances = generate_random_distances(num_cities)
    total_distance += tsp_brute_force(distances)
end_time = time.perf_counter()  # Record the end time
execution_time = end_time - start_time  # Calculate the execution time

# Display the randomly generated distance matrix
print("Randomly Generated Distance Matrix:")
for row in distances:
    print(row)

# Calculate and display the average distance and total execution time
average_distance_brute_force = total_distance / num_runs
print(f"Average Distance for Brute Force with {num_cities} cities over {num_runs} runs: {average_distance_brute_force}")
print(f"Total Execution Time for {num_runs} runs: {execution_time} seconds")
