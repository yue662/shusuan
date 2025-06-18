n,m=map(int,input().split())
dl0=[0]*n
da=[0]*n
for i in range(n):
    da[i]=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    dl0[a]+=1
    dl0[b]+=1
    da[a][b]=-1
    da[b][a]=-1
dout=da
for i in range(n):
    da[i][i]+=dl0[i]
for i in range(n):
    print(*dout[i])