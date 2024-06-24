'''
257. 二叉树的所有路径
    1
   / \
  2   3
  \
   5
输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]
'''

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        sub_path = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        return [str(root.val) + "->" + s for s in sub_path]