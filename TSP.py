from itertools import permutations

def calculate_total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    total_distance += distances[path[-1]][path[0]]  # Return to the starting city
    return total_distance

def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    all_cities = range(num_cities)

    # Generate all possible permutations of cities
    all_permutations = permutations(all_cities)

    min_distance = float('inf')
    best_path = None

    for path in all_permutations:
        current_distance = calculate_total_distance(path, distances)
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = path

    return best_path, min_distance

if __name__ == "__main__":
    # Example distances between cities (replace with your own distances)
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    best_path, min_distance = traveling_salesman_bruteforce(distances)

    print("Best Path:", best_path)
    print("Minimum Distance:", min_distance)