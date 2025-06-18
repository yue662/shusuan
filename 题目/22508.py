n,m=map(int,input().split())
dic={}
for i in range(n):
    dic[i]=[[],[]]
for i in range(m):
    a,b=map(int,input().split())
    dic[a][0].append(b)
    dic[b][1].append(a)
outl=[0]*n
def shan(k):
    for i in dic[k][1]:
        dic[i][0].remove(k)
    del dic[k]
t=0
while True:
    ol=[]
    for i in dic.keys():
        if len(dic[i][0])==0:
            ol.append(i)
    for i in ol:
        outl[i]=t
        shan(i)
    t+=1
    if len(dic)==0:
        break
print(n*100+sum(outl))