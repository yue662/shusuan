v,a=map(int,input().split())
sl=[]
for i in range(v):
    sl.append([i+1,set()])
for i in range(a):
    a,b=map(int,input().split())
    sl[b-1][1].add(a)
outl=[]
def shan(z):
    for i in sl:
        if z in i[1]:
            i[1].remove(z)
def check(sl):
    for i in sl:
        if len(i[1])==0:
            return [sl.index(i),i[0]]
while True:
    z=check(sl)
    del sl[z[0]]
    outl.append(z[1])
    shan(z[1])
    if len(sl)==0:
        break
for i in outl:
    print('v'+str(i),end=' ')