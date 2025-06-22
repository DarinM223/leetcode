# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode[T]:
    left: "TreeNode[T] | None"
    right: "TreeNode[T] | None"

    def __init__(self, x: T):
        self.val = x


def mDepth[T](root: TreeNode[T] | None) -> int:
    # if leaf node
    if root == None:
        return 0
    elif root.left == None and root.right == None:
        return 1
    elif root.left == None:
        return 1 + mDepth(root.right)
    elif root.right == None:
        return 1 + mDepth(root.left)

    return 1 + min(mDepth(root.left), mDepth(root.right))


class Solution:
    """
    Recursive solution
    Get the min of the depths of both children of the tree for each node
    """

    def minDepth[T](self, root: TreeNode[T]) -> int:
        return mDepth(root)
