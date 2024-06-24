'''
lc 删除链表中的节点
输入：head = [4,5,1,9], node = 5
输出：[4,1,9]

解释：从链表里删除一个节点 node 的最常见方法是修改之前节点的 next 指针，使其指向之后的节点。
4-> 5 ->9
4------>9
'''

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next