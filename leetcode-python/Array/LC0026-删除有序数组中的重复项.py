'''
lc26. 删除排序数组中的重复项
input: nums = [0,0,1,1,1,2,2,3,3,4]
output: 5, nums = [0,1,2,3,4]

标签：数组 双指针 从后遍历删除
'''
class Solution:
    @staticmethod
    def removeDuplicates(nums):
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == nums[i-1]:
                del nums[i]
        return len(nums)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution.removeDuplicates(nums))

