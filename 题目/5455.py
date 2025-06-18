class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
class BST:
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            self.insert(data)
    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)
    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
            if data > p.data:
                p.rchild = new_node
            else:
                p.lchild = new_node
sl=list(map(int,input().split()))
sls=[]
for i in sl:
    if i not in sls:
        sls.append(i)
bst=BST(sls)
st=bst.root
outs=[[st]]
while True:
    outs.append([])
    for i in outs[-2]:
        if i.lchild:
            outs[-1].append(i.lchild)
        if i.rchild:
            outs[-1].append(i.rchild)
    if len(outs[-1])==0:
        del outs[-1]
        break
out=[]
for i in outs:
    for j in range(len(i)):
        i[j]=i[j].data
    out=out+i
print(*out)