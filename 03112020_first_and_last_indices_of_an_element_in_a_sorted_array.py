'''
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given a sorted array, A, with possibly duplicated elements, find the indices of the 
first and last occurrences of a target element, x. Return -1 if the target is not found.

Example:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
Here is a function signature example:
'''

class Solution: 
    def getRange(self, arr, target):
        # Fill this in.
        # Use Binary Search Tree
        start = self.BinarySearchHelper(arr,target,0,len(arr)-1,True)
        end = self.BinarySearchHelper(arr,target,0,len(arr)-1,False)
        return([start,end])

    def BinarySearchHelper(self,arr,target,low,high,FindFirst):
        p = low+(high-low)//2
        if low > high:
            return(-1)
        if FindFirst:
            if (p==0 or arr[p-1] < target) and arr[p] == target:
                return(p)
            elif target > arr[p]:
                return self.BinarySearchHelper(arr,target,p+1,high,FindFirst)
            else:
                return self.BinarySearchHelper(arr,target,low,p-1,FindFirst)
        else:
            if (p==len(arr)-1 or arr[p+1] > target) and arr[p] == target:
                return(p)
            elif target < arr[p]:
                return self.BinarySearchHelper(arr,target,low,p-1,FindFirst)
            else:
                return self.BinarySearchHelper(arr,target,p+1,high,FindFirst)

# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]


# Note:
# 1. Classic Question and not the first time to do it
# 2. Time Complexity: O(logn)
# 3. Don't forget to write self. before the built-in function next time