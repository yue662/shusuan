n,m=map(int,input().split())
sl=list(map(int,input().split()))
for i in range(n):
    sl[i]=[sl[i],i]
while True:
    k=sl[-1]
    sl1=[]
    for i in sl:
        if i[0]>m:
            sl1.append([i[0]-m,i[1]])
    sl=sl1
    if len(sl)==0:
        print(k[1]+1)
        break