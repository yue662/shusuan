dic={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
n=int(input())
yl=[]
nl=[]
for _ in range(n):
    st=str(input())
    if '!' in st:
        nl.append([int(dic[st[0]]),int(dic[st[3]])])
    else:
        yl.append([int(dic[st[0]]),int(dic[st[3]])])
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
uf=UnionFind(26)
for i in yl:
    uf.union(i[0]-1,i[1]-1)
check=0
for i in nl:
    if uf.find(i[0]-1)==uf.find(i[1]-1):
        check=1
        print('False')
        break
if check==0:
    print('True')