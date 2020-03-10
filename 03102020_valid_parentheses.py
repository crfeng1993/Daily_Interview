'''
Hi, here's your problem today. This problem was recently asked by Uber:

Imagine you are building a compiler. Before running any code, the compiler must check that 
the parentheses in the program are balanced. Every opening bracket must have a corresponding 
closing bracket. We can approximate this using strings. 

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if 
the input string is valid. 

An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
'''

class Solution:
  def isValid(self, s):
    # Fill this in.
    # Use the stack
    checklist = []
    checkdict = {')':'(',']':'[','}':'{'}
        
    for item in s:
        if item in checkdict.values():
            checklist.append(item)
        else:
            if checklist and checklist[-1] == checkdict[item]:
                checklist=checklist[:-1]
            else:
                return False
        
    return (checklist == [])

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

# Note
# 1. Straightforward Question and Solution
# 2. Time Complexity = O(n)
# 3. return (checklist == []) is better than adding a new if statement