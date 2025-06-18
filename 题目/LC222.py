# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            sl=[[root]]
            while True:
                sl.append([])
                for i in sl[-2]:
                    if i.left:
                        sl[-1].append(i.left)
                    if i.right:
                        sl[-1].append(i.right)
                if len(sl[-1])==0:
                    return sum(len(j) for j in sl)