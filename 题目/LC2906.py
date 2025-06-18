class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n,m=len(grid),len(grid[0])
        sh=[0]*(n*m+1)
        sh[0]=1
        for i in range(n):
            for j in range(m):
                grid[i][j]%=12345
                sh[i*m+j+1]=sh[i*m+j]*grid[i][j]
                sh[i*m+j+1]%=12345
        eh=[0]*(n*m+1)
        eh[0]=1
        for i in range(n):
            for j in range(m):
                eh[i*m+j+1]=eh[i*m+j]*grid[n-1-i][m-1-j]
                eh[i*m+j+1]%=12345
        return [[(sh[i*m+j]*eh[(n-1-i)*m+m-1-j])%12345 for j in range(m)] for i in range(n)]