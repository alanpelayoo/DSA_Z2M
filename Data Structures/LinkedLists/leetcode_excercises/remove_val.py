from ll_example import LinkedList, ListNode

class Solution(object):
    def removeElements(self, head, val):
        #Create Dummy Node.
        dummy_head = ListNode(-1)
        dummy_head.next = head
 
        prev_node, curr_node = dummy_head, head
        while curr_node:
            if curr_node.val == val:
                prev_node.next = curr_node.next
            else:
                prev_node = curr_node
            curr_node = curr_node.next
        return dummy_head.next
    
#Linked List
linked_list_1 = LinkedList()
linked_list_1.append(1)
linked_list_1.append(2)
linked_list_1.append(6)
linked_list_1.append(3)
linked_list_1.append(4)
linked_list_1.append(6)
print(linked_list_1)

#Solution
sol = Solution()
new_head = sol.removeElements(linked_list_1.head, 6)

#Set new LL object head property to returned value
linked_list_1.head = new_head
print(linked_list_1)
