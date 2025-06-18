m,n,p,q=map(int,input().split())
sl=[]
for i in range(m):
    sl.append(list(map(int,input().split())))
nl=[]
for j in range(p):
    nl.append(list(map(int,input().split())))
outs=[]
for _ in range(m-p+1):
    outs.append([0]*(n-q+1))
for i in range(m-p+1):
    for j in range(n-q+1):
        for k in range(p):
            for l in range(q):
                outs[i][j]+=sl[i+k][j+l]*nl[k][l]
for out in outs:
    print(*out)