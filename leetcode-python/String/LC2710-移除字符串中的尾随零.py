'''
输入：num = "51230100"
输出："512301"
'''

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        i = len(num)-1
        while (num[i] == '0'):
            i -= 1
        return num[:i+1]


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        l = 0
        for i in range(len(num) - 1, -1, -1):
            if (num[i] != '0'):
                break
            l += 1
        return num[:len(num) - l]
