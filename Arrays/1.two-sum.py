#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        arr = []

        for i,x in enumerate(nums):
            arr.append([x, i])
        arr.sort()

        left,right = 0, len(nums)-1

        while left<right:
            sum = arr[left][0] + arr[right][0]
            
            if sum==target:
                return[arr[left][1],arr[right][1]]
            if sum>target:
                right -=1
            if sum<target:
                left +=1
            

                
        
# @lc code=end

