"""You are given two linked-lists representing two non-negative integers. The digits are stored in reverse
order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list."""
class ListNode:
  def __init__(self,x,nextNode = None):
    self.val = x
    self.next = nextNode
  
class Solution:
  def addTwoNumbers(self,l1, l2):
    if l1 == None:
      return l2
            
    if l2 == None:
      return l1
            
    sval = l1.val + l2.val
    if sval < 10:
      ansNode = ListNode(sval)
      ansNode.next = self.addTwoNumbers(l1.next, l2.next)
      return ansNode

    else:
      rval = l1.val + l2.val-10
      ansNode = ListNode(rval)
      ansNode.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
      return ansNode
    
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1,l2)

printList(result)
