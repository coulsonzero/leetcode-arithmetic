'''
示例 1 ：

输入：nums = [2,2,1]
输出：1
示例 2 ：

输入：nums = [4,1,2,1,2]
输出：4
'''


class Solution:
    def singleNumber(self, nums):
        m = {}
        for v in nums:
            m[v] = m.get(v, 0) + 1
        for k in m:
            if m[k] == 1:
                return k
        return -1

if __name__ == '__main__':
    nums = [4,1,2,1,2]
    s = Solution()
    print(s.singleNumber(nums))