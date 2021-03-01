#2. Add Two Numbers
#Medium
class Solution(object):
	def addTwoNumbers(self, l1, l2):
		prev = False
		head = ListNode()
		now = head
		while l1 or l2:
			val = int(prev)
			if l1:
				val += l1.val
				l1 = l1.next
			if l2:
				val += l2.val
				l2 = l2.next
			prev = val > 9
			now.next = ListNode(val % 10)
			now = now.next
		if prev:
			now.next = ListNode(1)
		return head.next

if __name__ == '__main__':
	solver = Solution()
	node = solver.addTwoNumbers()
