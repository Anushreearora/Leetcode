#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n = len(digits)

        for i in range(n-1,-1,-1):
            if digits[i] < 9:
                digits[i]+= 1
                return digits
            if i != 0 and digits[i] == 9:
                digits[i] = 0
            if i == 0 and digits[i] == 9:
                new = [0] * (n+1)
                new[0] = 1
                return new

        
# @lc code=end

