package main

import "sort"

/**
 * todo 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表
 * 输入：head = [-1,5,3,4,0]
 * 输出：[-1,0,3,4,5]
 */

func sortList(head *ListNode) *ListNode {
	// todo 添加至数组
	var nums []int
	for head != nil {
		nums = append(nums, head.Val)
		head = head.Next
	}

	sort.Ints(nums)

	// todo 生成新链表
	dummy := &ListNode{Next: nil}
	cur := dummy
	for i := 0; i < len(nums); i++ {
		cur.Next = &ListNode{Val: nums[i]}
		cur = cur.Next
	}

	return dummy.Next
}
