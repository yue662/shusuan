n,m=map(int,input().split())
cl=list(map(int,input().split()))
edges=[]
for _ in range(m):
    a,b=map(int,input().split())
    edges.append((a-1,b-1))
class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # 路径压缩
        return self.parent[p]
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] < self.rank[rootQ]:
                rootP, rootQ = rootQ, rootP  # 确保rootP是秩较高的树根
            self.parent[rootQ] = rootP
            if self.rank[rootP] == self.rank[rootQ]:
                self.rank[rootP] += 1  # 更新秩
z=UnionFind(n)
for a,b in edges:
    z.union(a,b)
pl={}
for i in range(n):
    pi=z.find(i)
    if pi not in pl:
        pl[pi]=cl[i]
    else:
        pl[pi]=min(pl[pi],cl[i])
print(sum(pl.values()))