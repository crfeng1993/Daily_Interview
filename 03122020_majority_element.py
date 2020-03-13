'''
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    #Fill this in.
    # 1. Hash Map
        countdict = {}
        for i in nums:
            countdict[i] = countdict.get(i,0)+1
            if countdict[i]>=len(nums)//2+1:
                return i
        return None

    # 2.Divide and Conquer
        if len(nums)==1:
                return nums[0]
            
        point = len(nums)//2
        ret1 = self.majorityElement(nums[:point])
        ret2 = self.majorityElement(nums[point:])

        if ret1 == ret2:
            return ret1
        return [ret2, ret1][nums.count(ret1)>len(nums)//2]

    #3. Boyer-Moore Majority Vote Algorithm
        number = nums[0]
        count = 0
        for item in nums:
            if item == number:
                count += 1
            elif count > 0:
                count -= 1
            else:
                number = item
                count += 1
        return number


# Note
# 1. Easy Question from Leetcode, and there are more than 3 ways to solve it
# 2. The Boyer-Moore Majority Vote has the lowest space complexity (O(1)) comparing to the other two (O(n) and O(logn))
# 3. However, I like the first solution, but always remeber the last one as final weapon