#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        res = []
        mp = {}

        for i in range(len(strs)):
            s = strs[i] 
            s = ''.join(sorted(s)) #sort the string and join

            if s not in mp:
                mp[s] = len(res) #get the index position of this new anagram
                res.append([]) #create a new subarray
            
            res[mp[s]].append(strs[i]) #find the position of the group and append to that subarray

        return res
        
# @lc code=end

