n,m=map(int,input().split())
sl=[0]
nl=[]
for i in range(n):
    r=int(input())
    sl.append(r+sl[-1])
    nl.append(r)
st=max(nl)
en=sl[-1]+1
outs=1
def ef(st,en):
    global outs
    mid=(st+en)//2
    fr=0
    k=1
    for j in range(n):
        if sl[j+1]-fr>mid:
            fr=sl[j]
            k+=1
    if k<=m:
        outs=mid
        en=mid
    else:
        st=mid+1
    if st>=en:
        return
    else:
        ef(st,en)
ef(st,en)
print(outs)