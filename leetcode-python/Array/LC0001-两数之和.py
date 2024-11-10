"""
lc 两数之和
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
"""


class Solution:
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    def twoSum(self, nums, target):
        m = {}                      # m = dict()
        for i, v in enumerate(nums):
            if target - v in m:     # if m.get(target - v) is not None:
                return [m[target - v], i]
            m[v] = i
        return None



if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))