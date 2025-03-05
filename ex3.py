#Question 1:

# The strategy used to grow arrays when full in the provided list_resize 
# function involves over-allocating memory proportional to the current 
# size of the list. This approach ensures that the list can accommodate 
# additional elements without needing to reallocate memory frequently, 
# which helps achieve linear-time amortized behavior for a sequence of 
# append operations.

# Explanation:
# Bypassing Reallocation:

# The function first checks if the current allocation is 
# sufficient to accommodate the new size without reallocation. If the 
# new size is less than or equal to the current allocation and greater 
# than or equal to half of the current allocation, it simply adjusts 
# the size without reallocating memory.

#if (allocated >= newsize && newsize >= (allocated >> 1)) {
#    assert(self->ob_item != NULL || newsize == 0);
#    Py_SET_SIZE(self, newsize);
#    return 0;
#}

# Over-Allocation Strategy:

# The function calculates the new allocated size using the 
# formula new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & 
# ~(size_t)3;. This formula over-allocates memory by adding an extra 
# 1/8th of the new size plus a small constant (6) and then rounding up 
# to the nearest multiple of 4.

#new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;

# Avoiding Over-Allocation:

# The function ensures that it does not over-allocate if 
# the new size is closer to the over-allocated size than to the old size.

#if (newsize - Py_SIZE(self) > (Py_ssize_t)(new_allocated - newsize))
#    new_allocated = ((size_t)newsize + 3) & ~(size_t)3;

# Handling Zero Size:

#If the new size is zero, the allocated size is set to zero.

#if (newsize == 0)
#    new_allocated = 0;

# Memory Reallocation:

# The function reallocates memory using PyMem_Realloc if 
# the new allocated size is within the allowable limits. If the 
# reallocation fails, it raises a memory error.

#if (new_allocated <= (size_t)PY_SSIZE_T_MAX / sizeof(PyObject *)) {
#    num_allocated_bytes = new_allocated * sizeof(PyObject *);
#    items = (PyObject **)PyMem_Realloc(self->ob_item, num_allocated_bytes);
#}
#else {
#    items = NULL;
#}
#if (items == NULL) {
#    PyErr_NoMemory();
#    return -1;
#}

# Growth Factor:
# The growth factor is approximately 1.125 (1 + 1/8), as indicated by 
# the term (newsize >> 3) in the over-allocation formula. This means 
# that the list grows by about 12.5% each time it needs to be resized.

#new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;





import sys

def get_capacity(lst):
    # Get size in bytes, subtract base list overhead, divide by size of each reference
    # On 64-bit Python, each reference is 8 bytes
    return (sys.getsizeof(lst) - sys.getsizeof([])) // 8

prev_capacity = 0
test_list = []

print("Starting with empty list")
print(f"Initial capacity: {get_capacity(test_list)}")


for i in range(64):
    test_list.append(i)
    current_capacity = get_capacity(test_list)
    
    if current_capacity != prev_capacity:
        print(f"Capacity changed at length {len(test_list)}: {prev_capacity} -> {current_capacity}")
        prev_capacity = current_capacity

print(f"Final list length: {len(test_list)}")
print(f"Final capacity: {get_capacity(test_list)}")

import timeit
import matplotlib.pyplot as plt
import numpy as np

# From the previous output, we know S=4 is the last size before expansion to 8
S = 4

# Arrays to store timing measurements
times_S_to_Splus1 = []  # Growing from S to S+1
times_Sminus1_to_S = [] # Growing from S-1 to S

# Measure S to S+1 growth 1000 times
for _ in range(1000):
    setup = f"test_list = list(range({S}))"
    stmt = f"test_list.append({S})"
    t = timeit.timeit(stmt=stmt, setup=setup, number=1) 
    times_S_to_Splus1.append(t * 1_000_000)  # Convert to microseconds

# Measure S-1 to S growth 1000 times
for _ in range(1000):
    setup = f"test_list = list(range({S-1}))"
    stmt = f"test_list.append({S-1})"
    t = timeit.timeit(stmt=stmt, setup=setup, number=1)
    times_Sminus1_to_S.append(t * 1_000_000)  # Convert to microseconds
# Create subplot for comparison
plt.figure(figsize=(12, 5))

# Calculate common x-axis limit
max_time = max(max(times_S_to_Splus1), max(times_Sminus1_to_S))
xlim = max_time * 0.4

plt.subplot(1, 2, 1)
plt.hist(times_S_to_Splus1, bins=30, alpha=0.7, label=f'S({S}) to S+1({S+1})')
plt.xlabel('Time (microseconds)')
plt.ylabel('Frequency')
plt.title('Distribution of Growth Times\nS to S+1')
plt.xlim(0, xlim)  # Use common limit
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(times_Sminus1_to_S, bins=30, alpha=0.7, label=f'S-1({S-1}) to S({S})')
plt.xlabel('Time (microseconds)')
plt.ylabel('Frequency')
plt.title('Distribution of Growth Times\nS-1 to S')
plt.xlim(0, xlim)  # Use common limit
plt.legend()

plt.tight_layout()
plt.show()

print(f"\nAverage time S to S+1: {np.mean(times_S_to_Splus1):.2f} microseconds")
print(f"Average time S-1 to S: {np.mean(times_Sminus1_to_S):.2f} microseconds")

# Answer to "Do you see any difference? Why?"
# Yes, there is a significant difference in timing distributions:
# 1. Growing from S-1 to S is faster because the list already has enough capacity
#    to accommodate the new element without needing reallocation
# 2. Growing from S to S+1 is slower because:
#    - Python lists use dynamic allocation with a growth factor
#    - When the internal array needs to grow, Python extends the existing array in memory
#    - The growth operation requires memory reallocation but stays in place
#    - This memory reallocation process explains the increased execution time we observe

