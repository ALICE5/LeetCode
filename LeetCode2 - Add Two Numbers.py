# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None 
        # point to the next ListNode and type is ListNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(-1)
        carry = 0

        while l1 or l2:
    	    a = l1.val if l1 else 0
    	    b = l2.val if l2 else 0

    	    sum = a + b + carry
    	    cur.next = ListNode(sum % 10) 
    	    cur = cur.next
    	    carry = sum // 10

    	    if l1:
    		    l1 = l1.next
    	    if l2:
    		    l2 = l2.next

        if carry > 0:
    	    cur.next = ListNode(1)

        return dummy.next


# test

l1_1 = ListNode(2)
l1_2 = ListNode(4)
l1_3 = ListNode(3)
l1_1.next = l1_2
l1_2.next = l1_3

l2_1 = ListNode(5)
l2_2 = ListNode(6)
l2_3 = ListNode(4)
l2_1.next = l2_2
l2_2.next = l2_3

l3_1 = Solution().addTwoNumbers(l1_1,l2_1)
while l3_1 != None:
	print(l3_1.val)
	l3_1 = l3_1.next

