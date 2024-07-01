"""
lc 移动零
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

标签：数组 双指针
"""


class Solution:
    def moveZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

