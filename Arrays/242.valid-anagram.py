#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        seen_s = {}
        seen_t = {}

        for i in range(len(s)):
            if s[i] in seen_s:
                seen_s[s[i]] += 1
            else:
                seen_s[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in seen_t:
                seen_t[t[i]] += 1
            else:
                seen_t[t[i]] = 1

        print(seen_s.keys())

        if seen_s.keys() == seen_t.keys():
            if seen_s.values() == seen_t.values():
                return True

        
        return False
        
# @lc code=end

