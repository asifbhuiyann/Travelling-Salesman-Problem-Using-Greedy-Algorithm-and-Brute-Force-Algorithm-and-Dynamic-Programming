import random
import timeit
import matplotlib.pyplot as plt

# Function to generate a worst-case distance matrix for n cities
def generate_worst_case_distances(n):
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = 100  # Set a high distance between all pairs of cities
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

# Calculate the worst-case distance for the worst case
def calculate_worst_distance_dynamic_programming(num_cities):
    distances = generate_worst_case_distances(num_cities)
    return tsp_dynamic_programming(distances)

# Number of cities for the worst case
num_cities_list = [3, 4, 5, 6]  # You can adjust this as needed

# Initialize a list to store the worst-case distances for Dynamic Programming Algorithm
worst_distances_dynamic_programming = []

# Calculate worst-case distances for Dynamic Programming Algorithm
for num_cities in num_cities_list:
    worst_distance_dynamic_programming = calculate_worst_distance_dynamic_programming(num_cities)
    worst_distances_dynamic_programming.append(worst_distance_dynamic_programming)

# Create a graph to visualize the worst-case distances for Dynamic Programming Algorithm
plt.figure(figsize=(10, 6))
plt.plot(num_cities_list, worst_distances_dynamic_programming, marker='o', label='Dynamic Programming')
plt.xlabel('Number of Cities')
plt.ylabel('Worst-Case Distance')
plt.title('Worst-Case Distance for Dynamic Programming Algorithm')
plt.legend()
plt.grid()
plt.show()
