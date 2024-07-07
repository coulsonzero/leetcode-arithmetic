'''
示例 1：
输入: scores = [2, 2, 3, 4, 4, 4, 5, 6, 6, 8], target = 4
输出: 3

示例 2：
输入: scores = [1, 2, 3, 5, 7, 9], target = 6
输出: 0
'''

class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        m = {}
        for i in range(len(scores)):
            m[scores[i]] = m.get(scores[i], 0) + 1

        return m.get(target, 0)