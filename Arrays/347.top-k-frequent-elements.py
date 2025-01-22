#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from heapq import heappush, heappop 

        #create hashmapwith values and frequencies
        freq = {}
        topkelements = []

        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        print(freq)

        #use minheap to get top k:
        for num,frequency in freq.items():
            heappush(topkelements,(frequency,num))
            if len(topkelements) > k:
                heappop(topkelements)
            
        top_numbers = []
        while topkelements:
            top_numbers.append(heappop(topkelements)[1])

        return top_numbers

 
    
# @lc code=end

