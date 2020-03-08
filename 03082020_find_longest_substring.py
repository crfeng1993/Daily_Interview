'''
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a string, find the length of the longest substring without repeating characters.

Here is an example solution in Python language. 
(Any language is OK to use in an interview, though we'd recommend Python as a generalist language utilized
 by companies like Google, Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)
Can you find a solution in linear time?
'''

class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
    dicts = {}
    start = 0
    max_len = 0
    for i,num in enumerate(s):
        if num in dicts and dicts[num] >= start:
            start = dicts[num]+1
        else:
            max_len = max(max_len, i-start+1)
        dicts[num]=i
    return(max_len) 

print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10


# Note:
# 1. For BruteFore Way, raises every possible substring and calculate it
# 2. The reason I stuck on it is that I didn't know which scenario the the right time to calculate the length
#    and which is the right moment for refreshing the pointers
# 3. Time Complexity: O(n)  Space Complexity: O(n)