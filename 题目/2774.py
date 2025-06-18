n,k=map(int,input().split())
sl=[]
for _ in range(n):
    sl.append(int(input()))
def erf(i):
    out=0
    for j in range(n):
        out+=sl[j]//i
    if out>=k:
        return True
    else:
        return False
all=sum(sl)
if k>all:
    print(0)
else:
    start=1
    end=max(sl)+1
    outs=1
    while start<end:
        mid=(start+end)//2
        if erf(mid):
            start=mid+1
            outs=mid
        else:
            end=mid
    print(outs)