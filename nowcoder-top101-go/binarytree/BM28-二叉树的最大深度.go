package main

import "math"

func maxDepth(root *TreeNode) int {
	// write code here
	if root == nil {
		return 0
	}
	return int(math.Max(float64(maxDepth(root.Left)), float64(maxDepth(root.Right)))) + 1
}
