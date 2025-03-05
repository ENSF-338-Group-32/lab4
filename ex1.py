import timeit
import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList: # Singly linked list class (Reused from ex7.py)
    def __init__(self):
        self.head = None

    def get_size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get_element_at_pos(self, pos):
        current = self.head
        count = 0
        while current:
            if count == pos:
                return current
            count += 1
            current = current.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def reverse_original(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead

class Array:
    def __init__(self):
        self.array = []

    def insert(self, data):
        self.array.append(data)

    def get_size(self):
        return len(self.array)

    def get_element_at_pos(self, pos):
        if pos < 0 or pos >= len(self.array):
            return None
        return self.array[pos]

    def print_array(self):
        for data in self.array:
            print(data, end=" -> ")
        print("None")

    def reverse(self):
        self.array = self.array[::-1]

def link_binary_search(self, target): # Binary search for linked list
    def search_recursive(start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        mid_node = self.get_element_at_pos(mid)
        if mid_node.data == target:
            return mid_node
        elif mid_node.data < target:
            return search_recursive(mid + 1, end)
        else:
            return search_recursive(start, mid - 1)

    size = self.get_size()
    return search_recursive(0, size - 1)

def arr_binary_search(self, target): # Binary search for array
    def search_recursive(start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        if self.array[mid] == target:
            return mid
        elif self.array[mid] < target:
            return search_recursive(mid + 1, end)
        else:
            return search_recursive(start, mid - 1)

    return search_recursive(0, len(self.array) - 1)

# Example usage:
print("Functionality test:")
sll = SinglyLinkedList()
sll.insert_head(1)
sll.insert_tail(2)
sll.insert_tail(3)
sll.insert_tail(4)
print("Original list:")
sll.print_list()
print(f'Data (Linked_list): {link_binary_search(sll,3).data}')


arr1 = Array()
arr1.insert(1)
arr1.insert(2)
arr1.insert(3)
arr1.insert(4)
print("Original array:")
arr1.print_array()
print(f'Position (Array): {arr_binary_search(arr1,3)}')

# Create 4 linked lists of lengths 1000, 2000, 4000, 8000
l1000_linked_lst = SinglyLinkedList()
for i in range(1000):
    l1000_linked_lst.insert_tail(i)

l2000_linked_lst = SinglyLinkedList()
for i in range(2000):
    l2000_linked_lst.insert_tail(i)

l4000_linked_lst = SinglyLinkedList()
for i in range(4000):
    l4000_linked_lst.insert_tail(i)

l8000_linked_lst = SinglyLinkedList()
for i in range(8000):
    l8000_linked_lst.insert_tail(i)

l1000_array = Array()
l2000_array = Array()
l4000_array = Array()
l8000_array = Array()

# Create 4 arrays of lengths 1000, 2000, 4000, 8000
l1000_linked_lst = Array()
for i in range(1000):
    l1000_array.insert(i)

l2000_linked_lst = Array()
for i in range(2000):
    l2000_array.insert(i)

l4000_linked_lst = Array()
for i in range(4000):
    l4000_array.insert(i)

l8000_linked_lst = Array()
for i in range(8000):
    l8000_array.insert(i)



# Function to measure the time taken for binary search on linked list and array
def measure_time(data_structure, search_function, size):
    target = random.randint(0, size - 1)
    start_time = timeit.default_timer()
    search_function(data_structure, target)
    end_time = timeit.default_timer()
    return end_time - start_time

# Measure times for linked lists
linked_list_sizes = [1000, 2000, 4000, 8000]
linked_list_times = []

for size in linked_list_sizes:
    linked_list = SinglyLinkedList()
    for i in range(size):
        linked_list.insert_tail(i)
    time_taken = measure_time(linked_list, link_binary_search, size)
    linked_list_times.append(time_taken)

# Measure times for arrays
array_sizes = [1000, 2000, 4000, 8000]
array_times = []

for size in array_sizes:
    array = Array()
    for i in range(size):
        array.insert(i)
    time_taken = measure_time(array, arr_binary_search, size)
    array_times.append(time_taken)

# Plotting the results
plt.plot(linked_list_sizes, linked_list_times, label='Linked List')
plt.plot(array_sizes, array_times, label='Array')
plt.xlabel('Size')
plt.ylabel('Time (seconds)')
plt.title('Binary Search Time Complexity')
plt.legend()
# Show the peak y values for each
plt.show()
# Print the peak y values for each
print(f'Peak time for Linked List: {max(linked_list_times)} seconds')
print(f'Peak time for Array: {max(array_times)} seconds')


#ex1 Part 4:
# The time complexity of the binary search algorithm is O(n) for linked lists.
# This is because in a linked list, when we perform a binary search, we must traverse the list to find the middle element, which takes O(n) time.
# We then recursively perform the same operation on the left or right half of the list, which halves the elemtes needed to be searched each time, O(n/2).
# This pattern creates a linear time complexity, were the time taken to travese to the middle dominates the time taken to search the list.
# This creates a situation of O(n)+O(logn)= O(n)