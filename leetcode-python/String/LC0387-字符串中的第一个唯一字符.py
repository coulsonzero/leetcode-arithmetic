'''
给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1
示例 1：
输入: s = "leetcode"
输出: 0
示例 2:
输入: s = "loveleetcode"
输出: 2
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for x in s:
            if s.find(x) == s.rfind(x):
                return s.find(x)
        return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = dict()
        for i in s:
            m[i] = m.get(i, 0) + 1
        for i, v in enumerate(s):
            if m[v] == 1:
                return i
        return -1