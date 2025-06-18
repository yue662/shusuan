n=int(input())
sl=[]
for i in range(n):
    sl.append(list(map(int,input().split())))
m=int(input())
for j in range(m):
    nl=list(map(int,input().split()))
    outs=[]
    nos=[]
    for k in range(n):
        if nl[k]==1:
            outs.append(set(sl[k][1:]))
        elif nl[k]==-1:
            nos.append(set(sl[k][1:]))
    if len(outs)==1:
        n1=outs[0]
    else:
        n1=outs[0].intersection(*outs[1:])
    if len(nos)==1:
        n2=nos[0]
    elif len(nos)==0:
        n2=set()
    else:
        n2=nos[0].union(*nos[1:])
    if len(n1)==0:
        print("NOT FOUND")
        continue
    pr=n1.difference(n2)
    if len(pr)==0:
        print("NOT FOUND")
    else:
        pr=list(pr)
        pr.sort()
        print(*pr)