n,m=map(int,input().split())
sl=[]
for i in range(n):
    sl.append([i,[],[]])
for i in range(m):
    a,b=map(int,input().split())
    sl[b][1].append(a)
    sl[a][2].append(b)
def shan(i):
    for j in sl[i][2]:
        sl[j][1].remove(i)
    sl[i]=0
while True:
    shl=[]
    for i in range(n):
        if sl[i]!=0:
            if len(sl[i][1])==0:
                shl.append(i)
    if len(shl)==0:
        break
    for i in shl:
        shan(i)
for i in range(n):
    if sl[i]!=0:
        print('Yes')
        break
else:
    print('No')
