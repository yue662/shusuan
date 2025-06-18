# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        outs=[[root]]
        while True:
            outs.append([])
            for i in range(len(outs[-2])):
                if outs[-2][i].left:
                    outs[-1].append(outs[-2][i].left)
                if outs[-2][i].right:
                    outs[-1].append(outs[-2][i].right)
            if len(outs[-1])==0:
                del outs[-1]
                break
        for i in range(len(outs)):
            for j in range(len(outs[i])):
                outs[i][j]=outs[i][j].val
        return outs