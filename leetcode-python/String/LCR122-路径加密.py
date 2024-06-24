'''
示例 1：
输入：path = "a.aef.qerf.bb"
输出："a aef qerf bb"
'''

class Solution:
    def pathEncryption(self, path: str) -> str:
        return path.replace('.', ' ')

