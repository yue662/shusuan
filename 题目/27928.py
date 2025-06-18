n=int(input())
dic={}
for _ in range(n):
    sl=list(map(int,input().split()))
    dic[sl[0]]=sl[1:]
for i in dic.keys():
    k=0
    for j in dic.keys():
        if i in dic[j]:
            k=1
            break
    if k==0:
        root=i
        break
def bf(ro,dict):
    if dict[ro]==[]:
        print(ro)
        return
    else:
        k=dict[ro]
        k.append(ro)
        k.sort()
        for i in k:
            if i==ro:
                print(i)
            else:
                bf(i,dict)
bf(root,dic)