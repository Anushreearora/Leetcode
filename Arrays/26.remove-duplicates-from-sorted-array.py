#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

#attempt 1 
        # tracking = {}

        # #loop through all elements and add to hashmap with key and count 
        # for i in range(len(nums)):
        #     if nums[i] in tracking.keys():
        #         continue
        #     else:
        #         tracking[nums[i]] = 1

        # #update array with first k elements based on number of keys
        # sorted_keys = sorted(tracking.keys())

        # for i in range(len(sorted_keys)):
        #     nums[i] = sorted_keys[i]
        
        # return len(sorted_keys)

#attempt 2
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j


# @lc code=end

