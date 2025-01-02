#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        j=len(nums)-1
        while(i<=j):
            if nums[i] ==val and nums[j]!=val:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
            if nums[j]==val:
                j-=1
            if nums[i]!=val:
                i+=1
        return i

# @lc code=end

