1) The complexity of arrays and linked lists vary gretly depending on useage, and the task given.

Arrays:

    Advantages:
        - Efficent random access due to its indexed data type, which in turn give it a O(1) at the worst case.
        - Ability to efficently edit any values O(1)

    Disadvantages:
        - Slow deletion and addition of elements, at O(n).  Especially true if element is placed/removed is not last element


Linked Lists:

    Advantages:
        - More Efficent Insertion and Deletion O(1) (*If position is know, else O(n))

    Disadvantages:
        - Slow indexing if values are not known (Pointer does not exist) O(n)
            Data must be traversed to find desired value

In the end, in terms of "complexity of task completion", it would be fair to say that Arrays hold the edge when we need a contiguous data stucture with very quick random access and editing.  However, when we intend to scale up our data strcture ot handle a greater variety of tasks, such as adding a node in the middle, constantly varying size of list, and restrcturing the list such as when sorting, we can typically rely on linked lists to provide a consistently better efficent execution of these tasks.

2) Assuming the array is mutable, we can perform the replce function through direct replacement, where the index that we desire is not erarsed, but has its data value overwritten.  This as a result prevent us from having to shift the array upon deletion and insertion, therefore reducing the time needed to perform this tasks.

However, if the array must be shifted, we can optimize this by inserting in front of old element requiring a shuffle, traversing to the next element (old element) and shifting back.  This prevents the traversing and shifting to be done for each seperate proccess, combining them into one task.  While not the most efficent, it congreagates tasks into a singular series of events, optimizing the replace function.

3) 
    1. Insertion sort
        - Must traverse through the array, tracking index to find suitable position (This is costly as traversing is costly on linked list)
        - O($n^2$)

    2. Merge sort
        - Does not rely on traversing, hence very relies less on linklist's weak features
        - Relies on the ability to quickly restructure lists, a strongpoint in linklist's capabilties
            - Split lists into sub arrays
            - Swap Elements
            - Rebuild and Merge Sub Arrays
        - O(n log(n))

    Based on this, it is fair to say that Merge Sort remains to be *more* suitable than Insertion, as it does not rely on the data structure's ability to traverse quickly, instead relying on the ability to modify, dismantle and rebuild the data structure, which Linked List, especially a doubly linked list excels at.

    Thus, based on this analysis it is fair to say, Mege sort is far more feasibile, where are Insertion sort must make very big modifications and adaptations to the data sturcture to work effectivly, as we would need the ability to recall a certain index upon completion of traversal, something linked lists, what been particularlly weak in.


    4) 
        Insertion Sort: An insertion sort will represent a complexity of O($n^2$) because using worst case:

            Traversal of linked list: O(n)
            Insertion Operation: O(1)
            Performing Sort for All Entities: O(n)

            O(n) * O(n) = O($n^2$)

        Merge Sort:  An merge sort will represent a complexity of O(nlogn) because using worst case:

            Finding the middle of linked list: O(n).
            Splitting the array: O(n) * O(log(n)): O(n log(n))
            Merging the array: O(n) * O(log(n)): O(n log(n))

            O(n) + O(n log(n)) + O(n log(n)) = O(n log(n))

        A merge sort remains the same complexity as a array, however, the complexity of finding the middle changes from O(1) to O(n)

        A insertion sort is similar where finding index takes O(n) instead of O(1), however shifting takes O(1) instead of O(n).
        However due to the traversing needed, we end up with the same complexity of O($n^2$)

    