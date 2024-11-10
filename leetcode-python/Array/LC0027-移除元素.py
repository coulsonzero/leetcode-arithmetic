'''
示例 1：

输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2,_,_]
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
        return l

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)

    