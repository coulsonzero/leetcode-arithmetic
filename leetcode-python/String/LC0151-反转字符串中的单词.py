'''
示例 1：

输入：s = "the sky is blue"
输出："blue is sky the"
示例 2：

输入：s = "  hello world  "
输出："world hello"
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])