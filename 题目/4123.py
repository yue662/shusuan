t=int(input())
for _ in range(t):
    dx=[-2,-2,-1,-1,1,1,2,2]
    dy=[-1,1,-2,2,-2,2,-1,1]
    def dfs(x,y,sl):
        global outs
        for i in range(8):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m and (nx,ny) not in sl:
                sl.append((nx,ny))
                if len(sl)==n*m:
                    outs+=1
                else:
                    dfs(nx,ny,sl)
                del sl[-1]
    n,m,k,l=map(int, input().split())
    outs=0
    dfs(k,l,[(k,l)])
    print(outs)