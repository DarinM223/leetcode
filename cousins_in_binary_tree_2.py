from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        # Set the root value to 0 since only parent's children are modified
        # so it will be skipped by the next parts.
        root.val = 0

        queue: deque[TreeNode] = deque()
        queue.append(root)
        while queue:
            buf: list[TreeNode] = []
            curr_level_sum = 0
            # Pop current depth level and accumulate sum for
            # all the nodes in the depth below the current level.
            for _ in range(len(queue)):
                node = queue.popleft()
                buf.append(node)
                if node.left:
                    queue.append(node.left)
                    curr_level_sum += node.left.val
                if node.right:
                    queue.append(node.right)
                    curr_level_sum += node.right.val
            for node in buf:
                # Subtract the children of the current parent node
                # to find the sum of the cousins for both children.
                node_sum = (
                    curr_level_sum
                    - (node.left.val if node.left else 0)
                    - (node.right.val if node.right else 0)
                )
                if node.left:
                    node.left.val = node_sum
                if node.right:
                    node.right.val = node_sum
        return root
