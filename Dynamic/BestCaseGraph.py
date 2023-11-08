import random
import timeit
import matplotlib.pyplot as plt

# Function to generate a best-case distance matrix for n cities
def generate_best_case_distances(n):
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distances[i][j] = j - i  # Nearest unvisited city is always the next city
            distances[j][i] = distances[i][j]
    return distances

# Dynamic Programming Algorithm with Memoization
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

# Calculate the best-case distance for the best case
def calculate_best_distance_dynamic_programming(num_cities, num_runs):
    total_distance = 0
    for _ in range(num_runs):
        distances = generate_best_case_distances(num_cities)
        total_distance += tsp_dynamic_programming(distances)
    return total_distance / num_runs

# Number of cities and runs for the best case
num_cities_list = [5, 10, 15, 20, 25]  # You can adjust this as needed
num_runs = 10   # Number of runs to calculate the average

# Initialize a list to store the best-case distances for Dynamic Programming Algorithm
best_distances_dynamic_programming = []

# Calculate best-case distances for Dynamic Programming Algorithm
for num_cities in num_cities_list:
    best_distance_dynamic_programming = calculate_best_distance_dynamic_programming(num_cities, num_runs)
    best_distances_dynamic_programming.append(best_distance_dynamic_programming)

# Create a graph to visualize the best-case distances for Dynamic Programming Algorithm
plt.figure(figsize=(10, 6))
plt.plot(num_cities_list, best_distances_dynamic_programming, marker='o', label='Dynamic Programming')
plt.xlabel('Number of Cities')
plt.ylabel('Best-Case Distance')
plt.title('Best-Case Distance for Dynamic Programming Algorithm')
plt.legend()
plt.grid()
plt.show()
