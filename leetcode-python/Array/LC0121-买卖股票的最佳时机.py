'''
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m, mp = prices[0], 0
        for p in prices:
            m = min(m, p)
            mp = max(mp, p - m)
        return mp