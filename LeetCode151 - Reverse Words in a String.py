class ListNode:
	def __init__(self,x):
		self.val = x
		self.next = None


class Solution:
	def reverseList(self,head):
		prev = None

		while head:
			temp = head.next 
			head.next = prev
			prev = head
			head = temp

		return prev


s_1 = ListNode('the')
s_2 = ListNode('sky')
s_3 = ListNode('is')
s_4 = ListNode('blue')

s_1.next = s_2
s_2.next = s_3
s_3.next = s_4

rs = Solution().reverseList(s_1)
while rs != None:
	print(rs.val)
	rs = rs.next
