'''
我们定义，在以下情况时，单词的大写用法是正确的：
1.全部字母都是大写，比如 "USA" 。
2.单词中所有字母都不是大写，比如 "leetcode" 。
3.如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false

示例 1：
输入：word = "USA"
输出：true
示例 2：
输入：word = "FlaG"
输出：false
'''



class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cnt = 0
        for c in word:
            if 'A' <= c and c <= 'Z':
                cnt += 1
        return cnt == len(word) or cnt == 0 or (cnt == 1 and 'A' <= word[0] and word[0] <= 'Z')