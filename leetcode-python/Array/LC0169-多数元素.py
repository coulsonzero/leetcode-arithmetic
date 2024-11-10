class Solution:
    def majorityElement(self, nums):
        m = {}
        for v in nums:
            m[v] = m.get(v, 0) + 1
            if m[v] > len(nums)/2:
                return v
        return -1