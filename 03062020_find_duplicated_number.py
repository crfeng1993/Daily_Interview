'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, 
find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''
import collections as ct

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #1. Sort—and-Scan
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return(nums[i])

        #2. Hash Map
        num_ct = ct.Counter(nums)
        num_list = set(nums)

        for i in num_list:
            if num_ct[i] > 1:
                return(i)

        #3. Floyd's Algorithm (Why do you use it?)
        pointer1 = nums[0]
        pointer2 = nums[0]
        while True:
            pointer1 = nums[pointer1]
            pointer2 = nums[nums[pointer2]]
            if pointer1 == pointer2:
                break
        
        pointer2 = nums[0]
        while pointer1 != pointer2:
            pointer1 = nums[pointer1]
            pointer2 = nums[pointer2]
        return(pointer1)

# Note:
# 1. Sort-and-Scan - Time Complexity: O(nlogn) (due to the sort)
# 2. Hash-map - Time Complexity: O(n) --I like it, fluid and effcient enough;
# 3. Floyd Algorithmn - Time Complexity：O(n) -- Best performance, but not easy to interpret;