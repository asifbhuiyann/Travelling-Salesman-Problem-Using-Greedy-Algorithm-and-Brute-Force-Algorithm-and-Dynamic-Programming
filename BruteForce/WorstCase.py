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

def tsp_brute_force_worst_case(distances):
    n = len(distances)
    min_path = float('inf')

    # Generate the worst-case permutation where all permutations need to be checked.
    worst_permutation = list(range(n))

    for perm in permutations(worst_permutation):
        current_distance = 0
        for i in range(n - 1):
            current_distance += distances[perm[i]][perm[i + 1]]
        current_distance += distances[perm[-1]][perm[0]]
        min_path = min(min_path, current_distance)

    return min_path

# Number of cities for the worst-case scenario
num_cities = 4

# Generate random distances and calculate the execution time for the worst-case scenario
start_time = time.perf_counter()  # Record the start time
distances = generate_random_distances(num_cities)
worst_case_distance = tsp_brute_force_worst_case(distances)
end_time = time.perf_counter()  # Record the end time
execution_time = end_time - start_time  # Calculate the execution time

# Display the randomly generated distance matrix
print("Randomly Generated Distance Matrix:")
for row in distances:
    print(row)

# Print the result including the worst-case distance and total execution time
print(f"Worst Case for Brute Force for {num_cities} cities: {worst_case_distance}")
print(f"Total Execution Time: {execution_time} seconds")
