'''
示例 1 ：

输入：nums = [2,2,1]
输出：1
示例 2 ：

输入：nums = [4,1,2,1,2]
输出：4
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = {}
        for i in range(len(nums)):
            m[nums[i]] = m.get(nums[i], 0) + 1
        for k in m:
            if m[k] == 1:
                return k
        return -1