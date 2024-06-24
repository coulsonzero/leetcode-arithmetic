'''
输入: s = "leetcode"
输出: false
'''


class Solution:
    def isUnique(self, s: str) -> bool:
        d = {}
        for i in s:
            if i in d:
                # d[i] += 1
                return False
            else:
                d[i] = 1
        return True