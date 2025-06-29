# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode[T]:
    def __init__(self, x: T):
        self.val = x
        self.left: "TreeNode[T] | None" = None
        self.right: "TreeNode[T] | None" = None


class Solution:

    def height[T](self, root: TreeNode[T] | None) -> int:
        # Leaf node
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced[T](self, root: TreeNode[T] | None) -> bool:
        if root == None:
            return True

        return (
            self.isBalanced(root.left)
            and self.isBalanced(root.right)
            and abs(self.height(root.left) - self.height(root.right)) <= 1
        )
