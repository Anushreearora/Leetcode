#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
#uses binary search
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high-low)//2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid+1
            if nums[mid] > target:
                high = mid-1
        
        return low
# @lc code=end

