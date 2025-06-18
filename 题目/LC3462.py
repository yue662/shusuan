class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n,m=len(grid),len(grid[0])
        sl=[]
        for i in range(n):
            for j in range(m):
                sl.append([grid[i][j],i])
        sl.sort(reverse=True)
        check=[0]*n
        check0=[True]*n
        outs=0
        k0=0
        if k0==k:
            return outs
        for i in range(n):
            if limits[i]==0:
                check0[i]=False
        for s in sl:
            if check0[s[1]]:
                outs+=s[0]
                check[s[1]]+=1
                k0+=1
                if check[s[1]]==limits[s[1]]:
                    check0[s[1]]=False
                if k0==k:
                    return outs