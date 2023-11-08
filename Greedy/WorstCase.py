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

def tsp_greedy_worst_case(distances):
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

    # worst-case scenario where the nearest unvisited city is the farthest away.
    for _ in range(n - 1):
        next_city = max(unvisited, key=lambda city: distances[current_city][city])
        current_distance += distances[current_city][next_city]
        unvisited.remove(next_city)
        current_city = next_city
    current_distance += distances[current_city][start]

    return current_distance

# Number of cities for the worst-case scenario
num_cities = 4

# random distances and calculate the execution time for the worst-case scenario
distances = generate_random_distances(num_cities)

start_time = time.perf_counter()  # start time
worst_case_distance = tsp_greedy_worst_case(distances)
end_time = time.perf_counter()  # end time
execution_time = end_time - start_time  # execution time

# Displaying randomly generated distance matrix
print("Randomly Generated Distance Matrix:")
for row in distances:
    print(row)

# result
print(f"Worst Case for Greedy Algorithm for {num_cities} cities: {worst_case_distance}")
print(f"Total Execution Time: {execution_time} seconds")
