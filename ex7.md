1) The given reverse() implementation has a complexity of O($n^2$) if we infer the complexity of the function get_element_at_pos(i) to be O(n) as it is on a standard linked list.
    - Due to the implmentation of the for loop, which iterates through the size of the linked list, we can classify this component to have a complexity of O(n)
    - Due to the use get_element_at_pos(i), which traverses a list, we can estimate a complexity of O(n).
        This code is called in conjunction, not in seprately to the for loop. Hence O(n) * O(n).
    -self.head = newhead at the bottom of the implementation can be considered O(1), however it is in addition to the for loop, hence O(1) + $O(n)^2$ = $O(n)^2$

    As a result, we can consider the complexity of this implementation of reverse() for a singly linked list to be $O(n)^2$
