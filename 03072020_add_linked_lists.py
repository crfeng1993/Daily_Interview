'''
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given two linked-lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.
    a = l1.val
    b = l2.val
    ret = ListNode((a+b+c)%10)
    c = (a+b+c)//10

    if l1.next or l2.next:
        if l1.next == None:
            l1.next = ListNode(0)
        if l2.next == None:
            l2.next = ListNode(0)
        ret.next = self.addTwoNumbers(l1.next,l2.next,c)
    return(ret)

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print (result.val)
    result = result.next

# Note:
# 1. This is a Recursive way to finish this question
# 2. Time Complexity: O(n) Space Complexity: O(n) (Using Stacking)
# 3. Understanding the recursion and it can be transformed into an interation
    