'''
lc 206. 反转链表
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

执行用时：40 ms, 在所有 Python3 提交中击败了84.54%的用户
'''

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

class Solution:
    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre