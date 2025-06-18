n=int(input())
def chl(l):
    t=0
    for i in sl2[l]:
        for j in range(i[1]):
            i[0].child.append(sl2[l+1][t][0])
            t+=1
def hb(l):
    if len(l.child)==0:
        out[0]+=l.val+' '
    else:
        for i in l.child:
            hb(i)
        out[0]+=l.val+' '
class treenode:
    def __init__(self,val):
        self.val=val
        self.child=[]
out=['']
for _ in range(n):
    sl=list(map(str,input().split()))
    sl1=[]
    for i in range(len(sl)//2):
        sl1.append([sl[2*i],int(sl[2*i+1])])
    for i in sl1:
        i[0]=treenode(i[0])
    sl2=[[sl1[0]]]
    del sl1[0]
    while sl1:
        k=0
        for i in sl2[-1]:
            k+=i[1]
        sl2.append(sl1[:k])
        del sl1[:k]
    for i in range(len(sl2)):
        chl(i)
    hb(sl2[0][0][0])
print(out[0])