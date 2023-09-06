from ll_example import LinkedList, ListNode

class Solution(object):
    def middle(self, head):
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

#Linked List
linked_list_1 = LinkedList()
linked_list_1.append(1)
linked_list_1.append(2)
linked_list_1.append(3)
linked_list_1.append(4)
linked_list_1.append(5)
linked_list_1.append(5)


print(linked_list_1)


sol = Solution()

sol.middle(linked_list_1.head)