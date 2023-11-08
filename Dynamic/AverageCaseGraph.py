import random
import timeit
import matplotlib.pyplot as plt

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

# Dynamic Programming Algorithm
def tsp_dynamic_programming(distances):
    n = len(distances)
    memo = {}

    def dp(mask, v):
        if mask == (1 << n) - 1:  # All cities have been visited
            return distances[v][0]  # Return to the starting city
        if (mask, v) in memo:
            return memo[(mask, v)]
        ans = float('inf')
        for u in range(n):
            if not (mask >> u) & 1:  # Check if city u is unvisited
                ans = min(ans, distances[v][u] + dp(mask | (1 << u), u))
        memo[(mask, v)] = ans
        return ans

    return dp(1, 0)

# Calculate the average distance for the average case
def calculate_average_distance(algorithm, num_cities, num_runs):
    total_distance = 0
    for _ in range(num_runs):
        distances = generate_random_distances(num_cities)
        total_distance += algorithm(distances)
    return total_distance / num_runs

# Number of cities and runs for the average case
num_cities_list = [5, 10, 15, 20, 25]  # You can adjust this as needed
num_runs = 5  # Number of runs for each case

# Initialize a list to store the average distances for Dynamic Programming
average_distances_dynamic = []

# Calculate average distances for Dynamic Programming Algorithm
for num_cities in num_cities_list:
    average_distance_dynamic = calculate_average_distance(tsp_dynamic_programming, num_cities, num_runs)
    average_distances_dynamic.append(average_distance_dynamic)

# Create a graph to visualize the average distances for Dynamic Programming Algorithm
plt.figure(figsize=(10, 6))
plt.plot(num_cities_list, average_distances_dynamic, marker='o', label='Dynamic Programming')
plt.xlabel('Number of Cities')
plt.ylabel('Average Distance')
plt.title('Average Distance for Dynamic Programming Algorithm')
plt.legend()
plt.grid()
plt.show()
