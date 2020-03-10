"""
Hi, here's your problem today. This problem was recently asked by Twitter:

A palindrome is a sequence of characters that reads the same backwards and forwards. 
Given a string, s, find the longest palindromic substring in s.

Example: 
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"
"""
class Solution:
    def longestPalindrome(self, s: str):
        #Brute force Way
        ret = [0,0]

        for i in range(len(s)):
            ret1 = self.loopforpalidrome(s,i,1)
            ret2 = self.loopforpalidrome(s,i,0)
            if ret1[1]>ret[1]:
                ret = ret1
            if ret2[1]>ret[1]:
                ret = ret2

        substring = s[ret[0]:ret[0]+ret[1]]
        return(substring)
        
    def loopforpalidrome(self,s,n,node):
        start = 0
        max_len = 0
        
        rg = min(len(s)-n-1-node,n)
        for j in range(rg+1):
            if s[n-j] == s[n+j+node]:
                if max_len < 2*j+1+node:
                    start = n-j
                    max_len = 2*j+1+node
            else:
                break

        return([start,max_len])     
    

# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar


# Note:
# 1. Now I know how a median question in Leetcode looks like...
# 2. The Brute Force Way is O(n^2)
# 3. For BF Way: Concentrate on the situation while it keeps unchanged,
#    instead of looking for the moment it changes
# 4. Manacher Algorithm is NB !!! But I can't understand it !!!
# 5. No repeated parts