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

# Greedy Algorithm
def tsp_greedy(distances):
    n = len(distances)
    start = 0
    unvisited = set(range(1, n))
    current_distance = 0
    current_city = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        current_distance += distances[current_city][next_city]
        unvisited.remove(next_city)
        current_city = next_city
    current_distance += distances[current_city][start]
    return current_distance

# Calculating the average distance for Greedy Algorithm
def calculate_average_greedy(num_cities, num_runs):
    total_distance = 0
    start_time = time.perf_counter()  # Recording the start time
    for _ in range(num_runs):
        distances = generate_random_distances(num_cities)
        total_distance += tsp_greedy(distances)
    end_time = time.perf_counter()  # Recording the end time
    execution_time = end_time - start_time  # Calculating the execution time

    return total_distance / num_runs, execution_time

num_cities = 4  # Number of cities and runs for the average case
num_runs = 10   # Number of runs to calculate the average

# Calculating average distance for Greedy Algorithm and total execution time
average_distance_greedy, total_execution_time = calculate_average_greedy(num_cities, num_runs)

# Displaying the randomly generated distance matrix
random_distance_matrix = generate_random_distances(num_cities)
print("Randomly Generated Distance Matrix:")
for row in random_distance_matrix:
    print(row)

# Printing the result
print(f"Average Distance for Greedy Algorithm with {num_cities} cities over {num_runs} runs: {average_distance_greedy}")
print(f"Total Execution Time for {num_runs} runs: {total_execution_time} seconds")
