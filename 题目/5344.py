a,b=map(int,input().split())
c=0
sl=[]
outs=[]
for i in range(a):
    sl.append(i+1)
for j in range(a):
    c=(c+b-1)%a
    outs.append(sl.pop(c))
    a-=1
print(*outs[:-1])