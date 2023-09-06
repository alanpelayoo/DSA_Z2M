class ListNode:
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
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

#Create list 1 
linked_list_1 = LinkedList()
linked_list_1.append(1)
linked_list_1.append(2)
linked_list_1.append(4)

#Create list 2
linked_list_2 = LinkedList()
linked_list_2.append(1)
linked_list_2.append(3)
linked_list_2.append(4)

print("LL 1", linked_list_1)
print("LL 2", linked_list_2)

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp_1 = l1
        temp_2 = l2
        prehead = ListNode(-1)
        prev = prehead

        while temp_1 or temp_2:
            if not temp_1:
                prev.next = temp_2
                temp_2 = temp_2.next
            elif not temp_2:
                prev.next = temp_1
                temp_1 = temp_1.next
            else:
                if temp_1.value < temp_2.value:
                    prev.next = temp_1

                    temp_1 = temp_1.next
                else:
                    prev.next = temp_2

                    temp_2 = temp_2.next
            prev = prev.next
        return prehead.next

sol = Solution()
new_h = sol.mergeTwoLists(linked_list_1.head, linked_list_2.head)  
result = ''
while new_h:
    result += str(new_h.value)
    if new_h.next is not None:
        result += ' -> '
    new_h = new_h.next
print(result)




