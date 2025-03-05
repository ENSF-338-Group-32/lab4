import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
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

    def reverse_optimized(self):
        past = None
        current = self.head

        while current:
            next_old = current.next  # Save next node
            current.next = past  # Reverse pointer
            past = current  # Move past forward
            current = next_old  # Move current forward

        self.head = past  # Update head to new first element

# Example usage:
print("Functionality test:")
sll = SinglyLinkedList()
sll.insert_head(1)
sll.insert_tail(2)
sll.insert_tail(3)
sll.insert_tail(4)
print("Original list:")
sll.print_list()
sll.reverse_original()
print("Original Reversed list:")
sll.print_list()
print("Optimized Re-Reversed list:")
sll.reverse_optimized()
sll.print_list()


# Create 4 linked lists of lengths 1000, 2000, 3000, 4000
l1000_linked_lst = SinglyLinkedList()
for i in range(1000):
    l1000_linked_lst.insert_tail(i)

l2000_linked_lst = SinglyLinkedList()
for i in range(2000):
    l2000_linked_lst.insert_tail(i)

l3000_linked_lst = SinglyLinkedList()
for i in range(3000):
    l3000_linked_lst.insert_tail(i)

l4000_linked_lst = SinglyLinkedList()
for i in range(4000):
    l4000_linked_lst.insert_tail(i)

print("Size of l1000_linked_lst:", l1000_linked_lst.get_size())
print("Size of l2000_linked_lst:", l2000_linked_lst.get_size())
print("Size of l3000_linked_lst:", l3000_linked_lst.get_size())
print("Size of l4000_linked_lst:", l4000_linked_lst.get_size())
        

# Timing reverse_original
time_reverse_original_1000 = timeit.timeit('l1000_linked_lst.reverse_original()', globals=globals(), number=100)
print("Done 1 OG")
time_reverse_original_2000 = timeit.timeit('l2000_linked_lst.reverse_original()', globals=globals(), number=100)
print("Done 2 OG")
time_reverse_original_3000 = timeit.timeit('l3000_linked_lst.reverse_original()', globals=globals(), number=100)
print("Done 3 OG")
time_reverse_original_4000 = timeit.timeit('l4000_linked_lst.reverse_original()', globals=globals(), number=100)
print("Done 4 OG")

# Timing reverse_optimized
time_reverse_optimized_1000 = timeit.timeit('l1000_linked_lst.reverse_optimized()', globals=globals(), number=100)
print("Done 1 OP")
time_reverse_optimized_2000 = timeit.timeit('l2000_linked_lst.reverse_optimized()', globals=globals(), number=100)
print("Done 2 OP")
time_reverse_optimized_3000 = timeit.timeit('l3000_linked_lst.reverse_optimized()', globals=globals(), number=100)
print("Done 3 OP")
time_reverse_optimized_4000 = timeit.timeit('l4000_linked_lst.reverse_optimized()', globals=globals(), number=100)
print("Done 4 OP")

# Plotting the results
sizes = [1000, 2000, 3000, 4000]
times_reverse_original = [time_reverse_original_1000, time_reverse_original_2000, time_reverse_original_3000, time_reverse_original_4000]
times_reverse_optimized = [time_reverse_optimized_1000, time_reverse_optimized_2000, time_reverse_optimized_3000, time_reverse_optimized_4000]

plt.plot(sizes, times_reverse_original, label='reverse_original')
plt.plot(sizes, times_reverse_optimized, label='reverse_optimized')
plt.xlabel('Size of Linked List')
plt.ylabel('Time (seconds)')
plt.title('Time to Reverse Linked List (100 runs)')
plt.legend()
plt.show()


"""
# Example usage:
sll = SinglyLinkedList()
sll.insert_head(1)
sll.insert_tail(2)
sll.insert_tail(3)
sll.insert_tail(4)
print("Original list:")
sll.print_list()
sll.reverse_original()
print("Reversed list:")
sll.print_list()

print("Original list:")
sll.reverse_optimized()
sll.print_list()
"""
