n=int(input())
sl=range(1,n+1)
outl=[]
def popi(l,pl,k):
    l.append(sl[k-1])
    t=len(l)
    if k==n:
        for _ in range(t):
            pl.append(l.pop())
        outl.append(pl)
        return
    else:
        l1=l.copy()
        pl1=pl.copy()
        for i in range(t+1):
            for _ in range(i):
                pl1.append(l1.pop())
            k+=1
            popi(l1,pl1,k)
            k-=1
            l1=l.copy()
            pl1=pl.copy()
popi([],[],1)
print(len(outl))