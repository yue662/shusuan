n=int(input())
edges=[]
for _ in range(n-1):
    a,b=map(int,input().split())
    edges.append([a,b])
    edges[-1].sort()
sl=list(map(int,input().split()))
e1=[]
for i in edges:
    if i[0] not in sl and i[1] not in sl:
        e1.append(i)
edges=e1
class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
    def find(self,p):
        if self.parent[p]!=p:
            self.parent[p]=self.find(self.parent[p])
        return self.parent[p]
    def union(self,p,q):
        rootp=self.find(p)
        rootq=self.find(q)
        if rootp!=rootq:
            if self.rank[rootp]<self.rank[rootq]:
                rootp,rootq=rootq,rootp
            self.parent[rootq]=rootp
            if self.rank[rootp]==self.rank[rootq]:
                self.rank[rootp]+=1
z=UnionFind(n)
for i in edges:
    z.union(i[0],i[1])
k=0
for i in range(n):
    if z.find(i)==z.find(0):
        k+=1
print(k)