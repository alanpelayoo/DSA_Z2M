"""
Remove Duplicates
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well. 

Example 1:

Input: head = [1,1,2]
Output: [1,2]
Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.val)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

class Solution(object):
    def deleteDuplicates(self, head):
        temp = head
        unique_set = set()
        while temp.next:
            unique_set.add(temp.val)
            if temp.next.val in unique_set:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head


linked_list_1 = LinkedList()
linked_list_1.append(1)
linked_list_1.append(2)
linked_list_1.append(4)
linked_list_1.append(3)
linked_list_1.append(4)
linked_list_1.append(2)
linked_list_1.append(5)

print(linked_list_1)

sol = Solution()
new_h = sol.deleteDuplicates(linked_list_1.head)
result = ''
while new_h:
    result += str(new_h.val)
    if new_h.next is not None:
        result += ' -> '
    new_h = new_h.next
print(result)