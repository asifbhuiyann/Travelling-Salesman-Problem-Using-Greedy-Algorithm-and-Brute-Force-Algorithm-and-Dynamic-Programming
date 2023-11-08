import random
import time

# Function to generate a random distance matrix for n cities
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

def tsp_dynamic_programming_worst_case(distances):
    n = len(distances)
    memo = {}

    # Generate the worst-case scenario where all possible paths need to be explored.
    def dp(mask, v):
        if mask == 2 ** n - 1:
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

# Number of cities for the worst-case scenario
num_cities = 4  # You can adjust this as needed

# Generate random distances and calculate the execution time for the worst-case scenario
start_time = time.perf_counter()  # Record the start time
distances = generate_random_distances(num_cities)
worst_case_distance = tsp_dynamic_programming_worst_case(distances)
end_time = time.perf_counter()  # Record the end time
execution_time = end_time - start_time  # Calculate the execution time

# Display the randomly generated distance matrix
print("Randomly Generated Distance Matrix:")
for row in distances:
    print(row)

# Print the result including the worst-case distance and total execution time
print(f"Worst Case for Dynamic Programming for {num_cities} cities: {worst_case_distance}")
print(f"Total Execution Time: {execution_time} seconds")
