n,k=map(int,input().split())
l1=[]
l2=[]
for i in range(n):
    a,b=map(int,input().split())
    l1.append([a,i+1])
    l2.append(b)
l1.sort(reverse=True)
l0=[]
for i in range(k):
    z=l1[i][1]
    l0.append([l2[z-1],z])
t=max(l0)
print(t[1])
