'''
@title: lc 旋转数组
@input: nums = [1,2,3,4,5,6,7], k = 3
@output: [5,6,7,1,2,3,4]
元素向右移动 k 个位置
'''


class Solution:
    @staticmethod
    def rotate(nums, k):
        m = k % len(nums)
        nums[:] = nums[-m:] + nums[:-m]


