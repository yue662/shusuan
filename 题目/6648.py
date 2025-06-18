def sh(l1,l2):
    li=min(l1)
    o=li[2]
    l2.append(l2[-1]+li[0])
    if len(l2)==n:
        return
    k2=min(sl[o])
    sl[o].remove(k2)
    l1[o][0]=k2-li[1]
    l1[o][1]=k2
    sh(l1,l2)
t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    if n==1:
        out=sum(int(input()) for i in range(m))
        print(out)
    else:
        sl=[]
        mi=0
        mins=[]
        for j in range(m):
            sl.append(list(map(int,input().split())))
            k=min(sl[j])
            sl[j].remove(k)
            mi+=k
            k1=min(sl[j])
            sl[j].remove(k1)
            mins.append([k1-k,k1,j])
        outs=[mi]
        sh(mins,outs)
        print(*outs)