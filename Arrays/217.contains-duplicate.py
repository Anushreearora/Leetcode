#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        distinct = set()

        for i in range(len(nums)):
            if nums[i] in distinct:
                return True
            else:
                distinct.add(nums[i])
        
        return False
        
# @lc code=end

