from ll_example import LinkedList, ListNode

class Solution(object):
    def isPalindrome(self, head):
        current = head
        prev = None
        length = 0
        #Reverse list, new nodes
        while current:
            new_node = ListNode(current.val)
            new_node.next = prev
            prev = new_node
            current = current.next
            length += 1
        
        temp_1 = head
        temp_2 = new_node

        if length % 2:
            #odd
            steps = (length-1)/2
        else:
            #even
            steps = length/2

        for i in range(int(steps)):
            if temp_1.val != temp_2.val:
                return False
            temp_1 = temp_1.next
            temp_2 = temp_2.next
        return True

elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#Linked List
linked_list_1 = LinkedList()
for i in elements:
    linked_list_1.append(i)

print(linked_list_1)


#Solution
sol = Solution()
print(sol.isPalindrome(linked_list_1.head))

