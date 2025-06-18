# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        else:
            sl=[[root]]
            while True:
                sl.append([])
                for i in sl[-2]:
                    if i.left:
                        sl[-1].append(i.left)
                    if i.right:
                        sl[-1].append(i.right)
                if len(sl[-1]) == 0:
                    del sl[-1]
                    break
            k=len(sl)
            for i in range(k):
                for j in range(len(sl[i])):
                    sl[i][j]=sl[i][j].val
            n=k//2
            for i in range(n):
                sl[i*2+1].reverse()
            return sl