'''
3. 无重复字符的最长子串
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d, ans, l = {}, 0, -1
        for r in range(len(s)):
            if s[r] in d:
                l = max(d[s[r]], l)
            d[s[r]] = r
            ans = max(ans, r - l)
        return ans


