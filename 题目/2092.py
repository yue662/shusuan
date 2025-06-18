while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    nl={}
    for i in range(n):
        sl=list(map(int,input().split()))
        for j in sl:
            if j not in nl:
                nl[j]=1
            else:
                nl[j]+=1
    nk=[]
    for k in nl:
        nk.append((nl[k],k))
    ma=max(nk)
    nk.remove(ma)
    ma=max(nk)
    ch=ma[0]
    outs=[]
    for k in nk:
        if k[0]==ch:
            outs.append(k[1])
    outs.sort()
    print(*outs)