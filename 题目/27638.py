n=int(input())
ys=0
sl=[]
nl=[]
for _ in range(n):
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        ys+=1
    sl.append([a,b])
    nl.append(a)
    nl.append(b)
for i in range(n):
    if i not in nl:
        st=i
        break
kl=[[st]]
while True:
    kl.append([])
    for i in range(len(kl[-2])):
        if sl[kl[-2][i]][0]!=-1:
            kl[-1].append(sl[kl[-2][i]][0])
        if sl[kl[-2][i]][1]!=-1:
            kl[-1].append(sl[kl[-2][i]][1])
    if len(kl[-1])==0:
        break
le=len(kl)-2
print(str(le)+' '+str(ys))