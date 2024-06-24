

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(i[::-1] for i in s.split())

        '''
        ans = []
        for i in s.split():
            ans.append(i[::-1])
        return ' '.join(ans)
        '''