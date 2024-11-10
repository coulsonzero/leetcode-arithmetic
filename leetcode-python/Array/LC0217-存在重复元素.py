'''
lc 存在重复元素
输入: [1,2,3,1]
输出: true

标签： 数组 排序 哈希表

解题思路：
1. 数组排序
2. 集合去重
3. 字典计数
'''

class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(nums) != len(set(nums))

class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for v in nums:
            d[v] = d.get(v, 0) + 1
        for key in d:
            if d[key] > 1:
                return True
        return False