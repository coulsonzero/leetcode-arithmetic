'''
lc26. 删除排序数组中的重复项
input: nums = [0,0,1,1,1,2,2,3,3,4]
output: 5, nums = [0,1,2,3,4]

标签：数组 双指针 从后遍历删除
'''
class Solution:
    @staticmethod
    def removeDuplicates(nums):
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                del nums[i]
        return len(nums)

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution.removeDuplicates(nums))

