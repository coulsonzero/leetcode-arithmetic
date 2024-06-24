'''
lc 验证回文串

输入: "A man, a plan, a canal: Panama"
输出: true
输入: "race a car"
输出: false
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = [i for i in s.lower() if i.isalnum()]
        return b == b[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = str.lower(re.sub('[\W_+]','',s))
        return res == res[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        b = ''
        for i in s.lower():
            if i.isalnum():
                b += i
        '''

        b = [i for i in s.lower() if i.isalnum()]
        ans = ''.join(b)

        l, r = 0, len(ans) - 1
        while l < r:
            if ans[l] != ans[r]:
                return False
            l += 1
            r -= 1
        return True


        '''
        for i in range(len(b) / 2):
            if b[i] != b[len(b) - i]:
                return False
        return True
        '''
    '''
    执行用时44 ms, 在所有 Python3 提交中击败了96.42%的用户
    '''
