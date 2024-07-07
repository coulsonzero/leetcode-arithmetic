"""
lc 移动零
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

标签：数组 双指针
"""


class Solution:
    def moveZeroes(self, nums):
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

