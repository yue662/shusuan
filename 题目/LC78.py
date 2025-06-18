class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        sl=[[nums]]
        for i in range(n):
            sl.append([])
            for j in sl[i]:
                for k in range(n-i):
                    no=j.copy()
                    del no[k]
                    if no not in sl[-1]:
                        sl[-1].append(no)
        for i in range(n+1):
            sl+=sl[0]
            del sl[0]
        return sl