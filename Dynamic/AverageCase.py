import random
import time

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

def tsp_dynamic_programming(distances):
    n = len(distances)
    memo = {}
    def dp(mask, v):
        if mask == 2**n - 1:
            return distances[v][0]
        if (mask, v) in memo:
            return memo[(mask, v)]
        ans = float('inf')
        for u in range(n):
            if not (mask >> u) & 1:
                ans = min(ans, distances[v][u] + dp(mask | (1 << u), u))
        memo[(mask, v)] = ans
        return ans
    return dp(1, 0)

# Number of cities and runs for the average case
num_cities = 5  # You can adjust this as needed
num_runs = 10   # Number of runs to calculate the average

# Generate random distances and calculate the execution time for Dynamic Programming
start_time = time.perf_counter()  # Record the start time
total_distance = 0
for _ in range(num_runs):
    distances = generate_random_distances(num_cities)
    total_distance += tsp_dynamic_programming(distances)
end_time = time.perf_counter()  # Record the end time
execution_time = end_time - start_time  # Calculate the execution time

# Display the randomly generated distance matrix
print("Randomly Generated Distance Matrix:")
for row in distances:
    print(row)

# Calculate and display the average distance and total execution time
average_distance_dynamic = total_distance / num_runs
print(f"Average Distance for Dynamic Programming with {num_cities} cities over {num_runs} runs: {average_distance_dynamic}")
print(f"Total Execution Time for {num_runs} runs: {execution_time} seconds")
