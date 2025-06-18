l,n,m=map(int,input().split())
sl=[]
for i in range(n):
    sl.append(int(input()))
sl.append(l)
def check(x):
    num=0
    nl=0
    for i in range(n+1):
        if sl[i]-nl<x:
            num+=1
        else:
            nl=sl[i]
    if num>m:
        return True
    else:
        return False
st=0
ed=l
outs=0
while st<ed:
    mid=(st+ed)//2
    if check(mid):
        ed=mid
    else:
        outs=mid
        st=mid+1
print(outs)