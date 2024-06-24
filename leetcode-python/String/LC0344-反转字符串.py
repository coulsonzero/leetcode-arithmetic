'''
lc 344. 反转字符串
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]

要求：原地修改数组，使用O(1)额外空间
标签：字符串 递归 双指针
'''


class Solution:
    '''
    解题思路：
    1. str.reverse() 原地反转
    2. s[:] = s[::-1] 切片反转
    3. 双指针 交换
    '''
    def reverseString(self, s):
        # s.reverse()
        # s[:] = s[::-1]

        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1