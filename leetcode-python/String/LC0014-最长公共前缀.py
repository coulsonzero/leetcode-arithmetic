'''
14 最长公共前缀 （困难）
示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s0 = strs[0]
        for i, v in enumerate(s0):
            for s in strs:
                if i == len(s) or s[i] != v:
                    return s0[:i]
        return s0

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         lcp = 0
#         for col in zip(*strs):
#             if len(set(col)) > 1:
#                 break
#             lcp += 1
#         return strs[0][:lcp]