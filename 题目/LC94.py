from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def zx(node: Optional[TreeNode],sl):
    if node:
        zx(node.left,sl)
        sl.append(node.val)
        zx(node.right,sl)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        outs=[]
        zx(root,outs)
        return outs