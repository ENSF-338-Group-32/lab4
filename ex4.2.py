import timeit
import random
import matplotlib.pyplot as plt

# Question 3: Inefficient and Efficient Search
# Inefficient: Linear Search (O(n))
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Efficient: Binary Search (O(log n))
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Question 4: Complexity
# - Linear Search: O(n) in the worst case (traverses entire array)
# - Binary Search: O(log n) in the worst case (divides search space in half)

# Question 5: Experiment to Compare Performance
array_size = 1000
num_tests = 100

# Generate a sorted array
sorted_array = list(range(array_size))
target = random.choice(sorted_array)

# Measure execution times
linear_times = timeit.repeat(lambda: linear_search(sorted_array, target), repeat=num_tests, number=1)
binary_times = timeit.repeat(lambda: binary_search(sorted_array, target), repeat=num_tests, number=1)

# Plot results
plt.hist(linear_times, bins=20, alpha=0.5, label="Linear Search")
plt.hist(binary_times, bins=20, alpha=0.5, label="Binary Search")
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency")
plt.legend()
plt.title("Execution Time Distribution for Search Algorithms")
plt.show()
