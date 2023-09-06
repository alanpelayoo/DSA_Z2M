"""
Remove Duplicates from a Singly Linked List
Given a singly linked list, write a function that removes all the duplicates. use this linked list .

Original Linked List - "1 -> 2 -> 4-> 3 -> 4->2"

Result Linked List - "1 -> 2 -> 4 -> 3

Big O: O(n), sets are key since they store only unique values and look up is o(1)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def remove_duplicates(self):
        if self.head is None:
            return
        temp = self.head
        uniques = set()
        while temp.next is not None:
            current = temp.next
            uniques.add(temp.value)
            if current.value in uniques:
                temp.next = current.next
                self.length -= 1
            else:
                temp = temp.next
        self.tail = temp

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)
linked_list.append(3)
linked_list.append(4)
linked_list.append(2)
linked_list.append(5)

print(linked_list)
linked_list.remove_duplicates()
print(linked_list)
print(linked_list.tail.value)
