from ll_example import LinkedList, ListNode

class Solution(object):
    """
    Reverse list, important aspect is to have a temp variable to shift current and point current.next
    """
    def reverse(self,head):
        prev = None
        current = head
        while current:
            #temp variable to save next node
            temp = current.next
            #point to prev node 
            current.next = prev
            #shift
            prev = current
            current = temp 
        return prev
    
#Linked List
linked_list_1 = LinkedList()
linked_list_1.append(1)
linked_list_1.append(2)
print(linked_list_1)


#Solution
sol = Solution()

linked_list_1.head = sol.reverse(linked_list_1.head)

print(linked_list_1)


