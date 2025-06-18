class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        stl=[]
        n=len(board)
        m=len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    stl.append([i,j])
        if len(word)==1 and len(stl)!=0:
            return True
        ol=[[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(i,j,k):
            for x,y in ol:
                if 0<=i+x<n and 0<=j+y<m:
                    if board[i+x][j+y]==word[k] and check[i+x][j+y]==0:
                        check[i+x][j+y]=1
                        if k==len(word)-1:
                            return True
                        if dfs(i+x,j+y,k+1):
                            return True
                        check[i+x][j+y]=0
            return False
        for o in stl:
            check=[[0]*m for _ in range(n)]
            check[o[0]][o[1]]=1
            if dfs(o[0],o[1],1):
                return True
        return False