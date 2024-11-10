class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        l = 2

        for r in range(2, len(nums)):
            if nums[l - 2] != nums[r]:
                nums[l] = nums[r]
                l += 1
        return l